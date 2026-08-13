return {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
            "nvim-lua/plenary.nvim",
            "MunifTanjim/nui.nvim",
            -- {"3rd/image.nvim", opts = {}}, -- Optional image support in preview window: See `# Preview Mode` for more information
    },
    opts = {
        window = {
            width = 30,
        },
        filesystem = {
            filtered_items = {
                visible = true,
                show_hidden_count = true,
                hide_dotfiles = false,
                hide_gitignored = false,
                hide_by_name = {
                  '.git',
                },
                never_show_by_pattern = {
                  ".null-ls_*",
                },
            }
        }
    },
}
