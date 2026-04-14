#!/usr/bin/env node
/**
 * Install or verify official Feishu OpenAPI MCP for Codex.
 *
 * Preference order:
 * 1. ~/.codex/config.toml
 * 2. ~/.claude.json (legacy fallback)
 */

import fs from "fs";
import os from "os";
import path from "path";

const CODEX_TOML_PATH = path.join(os.homedir(), ".codex", "config.toml");
const CLAUDE_JSON_PATH = path.join(os.homedir(), ".claude.json");

const REQUIRED_PRESETS = [
  "preset.light",
  "preset.default",
  "preset.im.default",
  "preset.base.default",
  "preset.base.batch",
  "preset.doc.default",
  "preset.task.default",
  "preset.calendar.default"
];

const REQUIRED_EXTRA_PERMISSIONS = [
  "docx.v1.documentBlock.patch",
  "docx.v1.documentBlockChildren.create",
  "docx.v1.documentBlockChildren.batchDelete"
];

const TOOL_LIST = [...REQUIRED_PRESETS, ...REQUIRED_EXTRA_PERMISSIONS].join(",");

function tomlString(value) {
  return `"${String(value).replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
}

function buildArgs(appId, appSecret) {
  return [
    "-y",
    "@larksuiteoapi/lark-mcp",
    "mcp",
    "-a",
    appId,
    "-s",
    appSecret,
    "-t",
    TOOL_LIST,
    "-c",
    "camel",
    "-l",
    "zh",
    "--token-mode",
    "tenant_access_token"
  ];
}

function readCodexToml() {
  if (!fs.existsSync(CODEX_TOML_PATH)) {
    return "";
  }
  return fs.readFileSync(CODEX_TOML_PATH, "utf8");
}

function checkCodexConfig(text) {
  const blockMatch = text.match(/^\[mcp_servers\.lark-mcp\][\s\S]*?(?=^\[|\z)/m);
  if (!blockMatch) {
    return { configured: false, reason: "lark-mcp is not configured in ~/.codex/config.toml." };
  }

  const block = blockMatch[0];
  const argsMissing = REQUIRED_PRESETS.filter((preset) => !block.includes(preset));
  if (argsMissing.length > 0) {
    return { configured: "incomplete", reason: `Missing required presets: ${argsMissing.join(", ")}` };
  }

  const permMissing = REQUIRED_EXTRA_PERMISSIONS.filter((perm) => !block.includes(perm));
  if (permMissing.length > 0) {
    return { configured: "incomplete", reason: `Missing required extra permissions: ${permMissing.join(", ")}` };
  }

  if (!block.includes("@larksuiteoapi/lark-mcp")) {
    return { configured: false, reason: "lark-mcp entry does not use the official @larksuiteoapi/lark-mcp package." };
  }

  if (!block.includes("camel")) {
    return { configured: "incomplete", reason: "Tool name case is not set to camel." };
  }

  if (!block.includes("tenant_access_token")) {
    return { configured: "incomplete", reason: "Token mode is not pinned to tenant_access_token." };
  }

  return { configured: true, reason: "Official lark-mcp configuration is present." };
}

function checkClaudeConfig() {
  if (!fs.existsSync(CLAUDE_JSON_PATH)) {
    return { configured: false, reason: "lark-mcp is not configured in ~/.claude.json." };
  }

  try {
    const json = JSON.parse(fs.readFileSync(CLAUDE_JSON_PATH, "utf8"));
    const entry = json?.mcpServers?.["lark-mcp"];
    if (!entry) {
      return { configured: false, reason: "lark-mcp is not configured in ~/.claude.json." };
    }
    const args = Array.isArray(entry.args) ? entry.args.join(" ") : "";
    if (!args.includes("@larksuiteoapi/lark-mcp")) {
      return { configured: false, reason: "lark-mcp entry does not use the official @larksuiteoapi/lark-mcp package." };
    }
    return { configured: true, reason: "Official lark-mcp configuration is present." };
  } catch (error) {
    return { configured: false, reason: `Failed to parse ~/.claude.json: ${error.message}` };
  }
}

function main() {
  const [appId, appSecret] = process.argv.slice(2);
  if (!appId || !appSecret) {
    console.error("Usage: node feishu-mcp-setup.js <app_id> <app_secret>");
    process.exit(1);
  }

  if (fs.existsSync(CODEX_TOML_PATH)) {
    const result = checkCodexConfig(readCodexToml());
    console.log(JSON.stringify({ target: CODEX_TOML_PATH, ...result }, null, 2));
    return;
  }

  const result = checkClaudeConfig();
  console.log(JSON.stringify({ target: CLAUDE_JSON_PATH, ...result }, null, 2));
}

main();
