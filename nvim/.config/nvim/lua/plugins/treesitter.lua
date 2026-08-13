return {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    opts = {
        ensure_installed = {
            "lua",
            "python",
            "javascript",
            "typescript",
            "html",
            "css",
            "tsx",
            "javascriptreact",
        },
        highlight = { enable = true },
        indent = { enable = true },
        autotag = { enable = true },
    }
}
