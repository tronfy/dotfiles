set --export SHELL /usr/bin/fish
set --export EDITOR code

set --export fish_greeting (fish -v)
set --export npm_config_prefix ~/.local

fish_add_path ~/.local/bin

source "$HOME/.config/fish/abbreviations.fish"
