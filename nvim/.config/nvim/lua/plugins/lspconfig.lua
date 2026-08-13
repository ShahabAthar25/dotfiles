return {
  {
    "williamboman/mason.nvim",
    config = function()
      require("mason").setup()
    end,
  },

  {
    "williamboman/mason-lspconfig.nvim",
    lazy = false,
    opts = {
      ensure_installed = {
        "lua_ls",
        "pyright",
        "ts_ls",
        "tailwindcss",
        "emmet_ls",
        "cssls",
        "gopls",
      },
      auto_install = true,
    },
  },

  {
    "neovim/nvim-lspconfig",
    config = function()
      require("config.lspconfig")
    end,
  },
}
