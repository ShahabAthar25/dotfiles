-- Configure vim settings
require("settings")

-- Load lazy.nvim
require("config.lazy")

-- Set up oil.nvim
require("oil").setup()

-- Set up bufferline.nvim
vim.opt.termguicolors = true
require("bufferline").setup({})

-- Markdown
-- require('render-markdown').setup({
--   completions = { lsp = { enabled = true } },
-- })

-- Import mappings
require("mappings")
