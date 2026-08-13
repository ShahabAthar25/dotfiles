-- Core
vim.keymap.set("n", "<C-s>", ":wa<CR>", { desc = "Writes all changes" })
vim.keymap.set("n", "<C-S-c>", '"+y', { desc = "Copy to system clipboard in normal mode" })
vim.keymap.set("v", "<C-S-c>", '"+y', { desc = "Copy to system clipboard in visual mode" })

-- Buffer
vim.keymap.set("n", "<leader>x", ":bd<CR>", { desc = "Closes active buffer" })
vim.keymap.set("n", "<leader>bn", ":enew<CR>", { desc = "Creates new buffer" })

-- Panels
vim.api.nvim_set_keymap("n", "<C-h>", "<C-w>h", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-j>", "<C-w>j", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-k>", "<C-w>k", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<C-l>", "<C-w>l", { noremap = true, silent = true })

-- Telescope
local builtin = require("telescope.builtin")
vim.keymap.set("n", "<leader>ff", builtin.find_files, { desc = "Telescope find files" })
vim.keymap.set("n", "<leader>fg", builtin.live_grep, { desc = "Telescope live grep" })
vim.keymap.set("n", "<leader>fb", builtin.buffers, { desc = "Telescope buffers" })

-- Oil File Explorer
vim.keymap.set("n", "-", "<CMD>Oil<CR>", { desc = "Open parent directory" })

-- Neo Tree
vim.keymap.set("n", "<leader>e", ":Neotree focus<CR>", { desc = "Open Neotree" })
vim.keymap.set("n", "<leader>ce", ":Neotree close<CR>", { desc = "Close Neotree" })

-- Buffer navigation
vim.keymap.set("n", "<Tab>", "<Cmd>BufferLineCycleNext<CR>", { desc = "Next buffer" })
vim.keymap.set("n", "<S-Tab>", "<Cmd>BufferLineCyclePrev<CR>", { desc = "Previous buffer" })

-- Copilot
-- Ctrl + J as auto suggestion completion
vim.keymap.set("i", "<C-J>", 'copilot#Accept("\\<CR>")', {
  expr = true,
  replace_keycodes = false,
})
vim.g.copilot_no_tab_map = true

-- Git
vim.keymap.set("n", "<leader>gs", ":G<CR>", { desc = "Open Git status" })
vim.keymap.set("n", "<leader>gc", ":G commit<CR>", { desc = "Git commit" })
vim.keymap.set("n", "<leader>gp", ":G push<CR>", { desc = "Git push" })
vim.keymap.set("n", "<leader>gl", ":G pull<CR>", { desc = "Git pull" })
vim.keymap.set("n", "<leader>gd", ":Gvdiffsplit<CR>", { desc = "Git diff" })
vim.keymap.set("n", "<leader>gt", ":G log<CR>", { desc = "Git log" })

-- Nvim autopairs
vim.keymap.set("n", "<leader>fw", function()
  require("nvim-autopairs.fastwrap").show(vim.api.nvim_get_current_buf())
end, { noremap = true, silent = true })
