return {
  "windwp/nvim-ts-autotag",
  ft = { "html", "javascript", "javascriptreact", "typescript", "typescriptreact", "tsx", "jsx" },
  dependencies = { "nvim-treesitter/nvim-treesitter" },
  config = function()
    require("nvim-treesitter.configs").setup({
      ensure_installed = { "tsx", "javascript", "html", "typescript" },
      highlight = { enable = true },
      indent = { enable = true },
      autotag = { enable = true },
    })
  end,
}
