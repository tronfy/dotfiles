export ZSH="$HOME/.oh-my-zsh"

### env ###
export EDITOR=nano
export PAGER=less

export GTK_USE_PORTAL=1
export MANGOHUD=1
export PROTON_EAC_RUNTIME="$HOME/.steam/steam/steamapps/common/Proton EasyAntiCheat Runtime"
export SDKMAN_DIR="$HOME/.sdkman"


### prompt ###
ZSH_THEME="spaceship"
SPACESHIP_CHAR_SYMBOL="λ"
SPACESHIP_CHAR_SYMBOL_ROOT="#"
SPACESHIP_CHAR_SUFFIX=" "
SPACESHIP_PROMPT_ADD_NEWLINE=false
SPACESHIP_PROMPT_ORDER=(
  user
  dir
  host
  git
  node
  rust
  exec_time
  line_sep
  jobs
  exit_code
  char
)


### history ###
export HISTFILE=~/.zsh_history
export HISTSIZE=10000
export SAVEHIST=10000


### plugins ###
plugins=(
  git
  zsh-syntax-highlighting
  zsh-autosuggestions
)

# zsh-autosuggestions
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=244"


### options ###
setopt autocd extendedglob nomatch rc_quotes
unsetopt beep correct correct_all notify


### source/init ###
source ~/.zsh_aliases
source $ZSH/oh-my-zsh.sh
source /usr/share/nvm/init-nvm.sh
eval "$(zoxide init zsh)"

# sdkman (must be at the end of the file)
[[ -s "$SDKMAN_DIR/bin/sdkman-init.sh" ]] && source "$SDKMAN_DIR/bin/sdkman-init.sh"
