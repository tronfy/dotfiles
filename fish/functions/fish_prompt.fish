function fish_prompt
    set_color --bold cyan; echo -n (whoami)
    set_color --bold white; echo -n ' in '
    set_color --bold magenta; echo -n (string replace "$HOME" '~' (pwd))
    set_color --bold white; echo -n ' $ '
    set_color normal
end
