-- Setting leaders for vim
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"

-- Set clipboard to system clipboard
-- vim.opt.clipboard = "unnamedplus"

-- Replace tab with spaces
vim.opt.expandtab = true
vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2

-- Set relative line numbers
vim.opt.number = true
vim.wo.relativenumber = true

-- Enable highlighting
-- vim.cmd("autocmd BufEnter,BufRead * :TSBufEnable highlight")

-- Create an augroup to manage your autocmds (optional but recommended)
local format_augroup = vim.api.nvim_create_augroup("FormatOnSave", { clear = true })

vim.api.nvim_create_autocmd("BufWritePre", {
  group = format_augroup,
  pattern = "*", -- Or specify specific file patterns, e.g., "*.js,*.jsx,*.ts,*.tsx"
  callback = function()
    vim.lsp.buf.format({ async = false })
  end,
  desc = "Autoformat on save",
})

-- Desplay error messages inline
vim.diagnostic.config({
  virtual_text = {
    prefix = "●",
  },
  signs = true,
  update_in_insert = false,
  float = {
    source = "always",
    border = "single",
    header = "",
    prefix = "",
  },
})
