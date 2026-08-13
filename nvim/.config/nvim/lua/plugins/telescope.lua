return {
    {
        'nvim-telescope/telescope.nvim',
        tag = '0.1.8',
        dependencies = { 'nvim-lua/plenary.nvim' }
    },

    {
        'nvim-telescope/telescope-ui-select.nvim',
        config = function ()
            require("telescope").setup {
              extensions = {
                ["ui-select"] = {
                  require("telescope.themes").get_dropdown {
                    -- even more opts
                  }
                }
              },
              pickers = {
                  find_files = {
                      hidden = true,
                      find_command = {
                        'rg', '--files', '--hidden', '--glob', '!.git/', '--glob', '!__pycache__/', '--glob', '!node_modules/'
                      },
                  }
              },
            }

            require("telescope").load_extension("ui-select")
        end
    }
}
