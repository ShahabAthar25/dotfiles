local capabilities = require("cmp_nvim_lsp").default_capabilities()

-- LSP Servers setup
vim.lsp.config("lua_ls", {
  capabilities = capabilities,
})
vim.lsp.config("pyright", {
  capabilities = capabilities,
  settings = {
    python = {
      analyzerRemoved = {
        unreachableCode = false,
      },
    },
  },
})
vim.lsp.config("eslint_d", {
  capabilities = capabilities,
})
vim.lsp.config("ts_ls", {
  capabilities = capabilities,
})
vim.lsp.config("tailwindcss", {
  capabilities = capabilities,
})
vim.lsp.config("emmet_ls", {
  capabilities = capabilities,
})
vim.lsp.config("html", {
  filetypes = { "html", "javascript", "javascriptreact", "typescript", "typescriptreact" },
  init_options = {
    provideFormatter = true,
  },
  capabilities = capabilities,
})
vim.lsp.config("cssls", {
  capabilities = capabilities,
})

-- Command to restart all LSP clients except null-ls and copilot
vim.api.nvim_create_user_command("LspRestartClean", function()
  local clients = vim.lsp.get_active_clients()
  for _, client in pairs(clients) do
    if client.name ~= "null-ls" and client.name ~= "copilot" then
      vim.lsp.stop_client(client.id, true)
    end
  end
end, {})

-- Lsp Keybindings
vim.keymap.set("n", "K", vim.lsp.buf.hover, { desc = "Gives information about symbol under the cursor" })
vim.keymap.set("n", "gi", vim.lsp.buf.implementation, {})
vim.keymap.set({ "n", "v" }, "<leader>ca", vim.lsp.buf.code_action, {})
vim.keymap.set({ "n" }, "<leader>rn", vim.lsp.buf.rename, {})
vim.keymap.set("n", "<leader>ge", function()
  vim.diagnostic.open_float()
end, { desc = "Open diagnostic float" })
