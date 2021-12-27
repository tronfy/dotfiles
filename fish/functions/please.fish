function please --description 'run previous command as sudo'
  eval command sudo $history[1]
end
