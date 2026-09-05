# Export default variables
export XDG_CONFIG_HOME="$HOME/.config"
export TERM='xterm-256color'
export EDITOR='nvim'
export VISUAL='nvim'
export SUDO_EDITOR="nvim"

# export NVM_DIR="$HOME/.config/nvm"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# Set the directory of zinit pkg manager
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git";

# Download zinit if not installed
if [ ! -d "$ZINIT_HOME" ]; then
	mkdir -p "$(dirname $ZINIT_HOME)";
	git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME";
fi

# Source zinit
source "${ZINIT_HOME}/zinit.zsh"

# ZSH plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions

# Enable auto completions
autoload -U compinit && compinit

# Initialize starship prompt
eval "$(starship init zsh)"

# Key bindings
bindkey -v

bindkey '^p' history-search-backward
bindkey '^n' history-search-forward

bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char

bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

bindkey -r "\C-l"

# History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTUP=erase

setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

# Completion Styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors '${(s.:.)LS_COLORS}'

# Aliases
alias ls="ls --color"
alias vim=nvim
alias activate='source $(poetry env info --path)/bin/activate'
alias celar='clear'

# pnpm
export PNPM_HOME="$HOME/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end
