function yta --description 'download high quality audio from youtube'
  youtube-dl -f bestaudio --yes-playlist --extract-audio --add-metadata $argv
end
