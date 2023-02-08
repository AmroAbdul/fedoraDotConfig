set -g fish_color_autosuggestion 555 yellow
set -g fish_color_command 5f87d7
set -g fish_color_comment 808080
set -g fish_color_cwd 87af5f
set -g fish_color_cwd_root 5f0000
set -g fish_color_error 870000 --bold
set -g fish_color_escape af5f5f
set -g fish_color_history_current 87afd7
set -g fish_color_host 5f87af
set -g fish_color_match d7d7d7 --background=303030
set -g fish_color_normal normal
set -g fish_color_operator d7d7d7
set -g fish_color_param 5f87af
set -g fish_color_quote d7af5f
set -g fish_color_redirection normal
set -g fish_color_search_match --background=purple
set -g fish_color_status 5f0000
set -g fish_color_user 5f875f
set -g fish_color_valid_path --underline

set -g fish_color_dimmed 555
set -g fish_color_separator 999
# Git prompt status
set -g __fish_git_prompt_showdirtystate 'yes'
set -g __fish_git_prompt_showupstream auto
set -g pure_git_untracked_dirty false

starship init fish | source



alias s 'sudo'
alias v 'vim'
alias cpdir 'cp -r '
alias py 'python'
alias rmdir 'rm -rf '
alias systemctl 'sudo systemctl '
alias init 'git init'
alias clone 'git clone'
alias clone_branch 'git clone-branch'
alias install 'sudo dnf install '
alias remove 'sudo dnf remove '
alias list 'sudo yum list installed '
alias search 'sudo dnf search '
alias run 'flatpak run '
alias removeflat 'sudo flatpak uninstall '
alias installflat 'sudo flatpak install '
alias .CONFIG 'cd ~/.config'
alias Downloads 'cd ~/Downloads'
alias Documents 'cd ~/Documents'
alias . 'cd '
alias q 'exit'
alias x 'exit'
alias code 'code -r '

alias ls 'exa --icons -1 -a'
alias lsdir 'exa --icons'
alias lsa 'exa --icons -1 -l -a'
alias cat 'bat '
alias vim 'nvim'
alias doomemacs 'emacs'
alias spacemacs 'emacs'
alias emacs 'emacs'
alias mpvAudio 'mpv --no-video '
alias mpvVideo'mpv '
alias c 'clear'
alias h 'history'
alias pull 'git pull '
alias push 'git push '
alias checkout 'git checkout '
# alias switch='git switch '
alias addall 'git add .'
alias add 'git add'
alias make_install 'sudo make install'
# alias 'status'  'git status'
alias branch 'git branch'
alias commit 'git commit -m'
alias reboot 'sudo /sbin/reboot'
alias poweroff 'sudo /sbin/poweroff'
alias shutdown 'sudo /sbin/shutdown'
alias wget 'wget -c'
alias ports 'netstat -tulanp'
alias j 'jobs -l'
alias ويب "brave-browser"
alias egrep 'egrep --colour=auto'
alias fgrep 'fgrep --colour=auto'
alias start_docker 'sudo systemctl start --now docker'
alias fetch 'git fetch'
alias tag 'git tag'
alias newtag'git tag -a'
alias yta-aac "yt-dlp --extract-audio --audio-format aac "
alias yta-best "yt-dlp --extract-audio --audio-format best "
alias yta-flac "yt-dlp --extract-audio --audio-format flac "
alias yta-m4a "yt-dlp --extract-audio --audio-format m4a "
alias yta-mp3 "yt-dlp --extract-audio --audio-format mp3 "
alias yta-opus "yt-dlp --extract-audio --audio-format opus "
alias yta-vorbis "yt-dlp --extract-audio --audio-format vorbis "
alias yta-wav "yt-dlp --extract-audio --audio-format wav "
alias ytv-best "yt-dlp -f bestvideo+bestaudio "
alias tobash "sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh "sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"
alias tofish "sudo chsh $USER -s /bin/fish && echo 'Now log out.'"
alias topwsh 'sudo chsh amro -s /usr/bin/pwsh && echo '\''Now log out.'\'
alias vi "vim"
alias totalusage='df -hl --total | grep total'
alias usage='du -ch | grep total'
alias wifikey="sudo grep -r '^psk=' /etc/NetworkManager/system-connections/"

# alias disks 'echo "╓───── m o u n t . p o i n t s"; \
# 			 echo "╙────────────────────────────────────── ─ ─ "; \
# 			 lsblk -a; echo ""; \
# 			 echo "╓───── d i s k . u s a g e";\
# 			 echo "╙────────────────────────────────────── ─ ─ "; \
# 			 df -h;'
# # alias ~ 'cd ~/'
# alias / 'cd /'
alias TEMP 'cd /tmp'
# alias pip 'function _pip(){
#     if [ $1 = "search" ]; then
#         pip_search "$2";
#     else pip "$@";
#     fi;
# };_pip'



# Compress () 
# {
# if [ -f $1 ]  ; then
#    	case $1 in
#    	*.tar.bz2)     tar $1    ;;
#    	*.tar.gz)      tar $1    ;;
#    	*.bz2)         bunzio2 $1 ;;
#   	*.rar)         rar x $1 ;;
#    	*.gz)          gunzip $1  ;;
#    	*.tar)         tar $1     ;;
#    	*.tbz2)        tar $1     ;;
#    	*.tgz)         tar $1     ;;
#    	*.zip)         zip $1   ;;
#    	*.Z)            compress $1 ;;
# 	*.7z)          7z x $1      ;;
# 	*)             echo "'$1' cannot be compressed via ex()" ;;
#    	esac
# else  
#     echo "'$1' is not a valid file"
# fi


# }
# Extract ()
# {
#   if [ -f $1 ] ; then
#     case $1 in
#       *.tar.bz2)   tar xjf $1   ;;
#       *.tar.gz)    tar xzf $1   ;;
#       *.bz2)       bunzip2 $1   ;;
#       *.rar)       unrar x $1     ;;
#       *.gz)        gunzip $1    ;;
#       *.tar)       tar xf $1    ;;
#       *.tbz2)      tar xjf $1   ;;
#       *.tgz)       tar xzf $1   ;;
#       *.zip)       unzip $1     ;;
#       *.Z)         uncompress $1;;
#       *.7z)        7z x $1      ;;
#       *)           echo "'$1' cannot be extracted via ex()" ;;
#     esac
#   else
#     echo "'$1' is not a valid file"
#   fi
# }
# function source ($1){
   
# }
# Navigation
function ..    ; cd .. ; end
function ...   ; cd ../.. ; end
function ....  ; cd ../../.. ; end
function ..... ; cd ../../../.. ; end
abbr g git
