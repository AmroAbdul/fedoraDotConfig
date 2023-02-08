#
# ~/.bashrc
#
# If not running interactively, don't do anything

export BROWSER="opera-developer"
export EDITOR="code -r"
export USERNAME="abdulvahitamro"
export githubURL="https://github.com/abdulvahitamro/"

[[ $- != *i* ]] && return



 ## ??????
 colors() {
	local fgc bgc vals seq0

	printf "Color escapes are %s\n" '\e[${value};...;${value}m'
	printf "Values 30..37 are \e[33mforeground colors\e[m\n"
	printf "Values 40..47 are \e[43mbackground colors\e[m\n"
	printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

	# foreground colors
	for fgc in {30..37}; do
		# background colors
		for bgc in {40..47}; do
			fgc=${fgc#37} # white
			bgc=${bgc#40} # black

			vals="${fgc:+$fgc;}${bgc}"
			vals=${vals%%;}

			seq0="${vals:+\e[${vals}m}"
			printf "  %-9s" "${seq0:-(default)}"
			printf " ${seq0}TEXT\e[m"
			printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
		done
		echo; echo
	done
}
alias pip='function _pip(){
    if [ $1 = "search" ]; then
        pip_search "$2";
    else pip "$@";
    fi;
};_pip'
CloneRepo() {
local repoName="$1"
local userName="AmroAbdul"
local gitHost="github.com"
git clone "https://$gitHost/$userName/$1";
cd $1;
}
# function genplaylist() {
# 	cd ~/music
# 	find . -name '*.mp3' -o -name '*.flac'|sed -e 's%^./%%g' > ~/.config/mpd/playlists/all.m3u
# 	mpc clear
# 	mpc load all.m3u
# 	mpc update
# }
# function getGeoLocation() {
# 	curl https://ipinfo.io/loc
# }

function gitforge() {
	[ ! -d .git ] && echo "not a git repo" && return
	gitauthor=`git config user.name`
	printf "author ($gitauthor): "
	read -r author
	author=${author:=$gitauthor}
	gitemail=`git config user.email`
	printf "email ($gitemail):"
	read -r email
	email=${email:=$gitemail}
	now=`date -Is`
	printf "date ($now):"
	read -r date
	date=${date:=$now}
	echo "\nhacking time as: $author <$email> $date\n"
	export GIT_AUTHOR_DATE=$date
	export GIT_AUTHOR_EMAIL=$email
	export GIT_AUTHOR_NAME=$author
	export GIT_COMMITTER_DATE=$date
	export GIT_COMMITTER_EMAIL=$email
	export GIT_COMMITTER_NAME=$author
	[ ! "$1" ] && git commit || git commit -S$1
	unset GIT_AUTHOR_DATE
	unset GIT_AUTHOR_EMAIL
	unset GIT_AUTHOR_NAME
	unset GIT_COMMITTER_DATE
	unset GIT_COMMITTER_EMAIL
	unset GIT_COMMITTER_NAME
}



### bash completion ####
[ -r /usr/share/bash-completion/bash_completion ] && . /usr/share/bash-completion/bash_completion


# Change the window title of X terminals
case ${TERM} in
	xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|interix|konsole*)
		PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
		;;
	screen*)
		PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
		;;
esac

use_color=true

# Set colorful PS1 only on colorful terminals.
# dircolors --print-database uses its own built-in database
# instead of using /etc/DIR_COLORS.  Try to use the external file
# first to take advantage of user additions.  Use internal bash
# globbing instead of external grep binary.
safe_term=${TERM//[^[:alnum:]]/?}   # sanitize TERM
match_lhs=""
[[ -f ~/.dir_colors   ]] && match_lhs="${match_lhs}$(<~/.dir_colors)"
[[ -f /etc/DIR_COLORS ]] && match_lhs="${match_lhs}$(</etc/DIR_COLORS)"
[[ -z ${match_lhs}    ]] \
	&& type -P dircolors >/dev/null \
	&& match_lhs=$(dircolors --print-database)
[[ $'\n'${match_lhs} == *$'\n'"TERM "${safe_term}* ]] && use_color=true

if ${use_color} ; then
	# Enable colors for ls, etc.  Prefer ~/.dir_colors #64489
	if type -P dircolors >/dev/null ; then
		if [[ -f ~/.dir_colors ]] ; then
			eval $(dircolors -b ~/.dir_colors)
		elif [[ -f /etc/DIR_COLORS ]] ; then
			eval $(dircolors -b /etc/DIR_COLORS)
		fi
	fi

	if [[ ${EUID} == 0 ]] ; then
		PS1='\[\033[01;31m\][\h\[\033[01;36m\] \W\[\033[01;31m\]]\$\[\033[00m\] '
	else
		PS1='\[\033[01;32m\][\u@\h\[\033[01;37m\] \W\[\033[01;32m\]]\$\[\033[00m\] '
	fi

else
	if [[ ${EUID} == 0 ]] ; then
		# show root@ when we don't have colors
		PS1='\u@\h \W \$ '
	else
		PS1='\u@\h \w \$ '
	fi
fi

unset use_color safe_term match_lhs sh


# # ex - archive extractor
# # usage: ex <file>
Extract ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

Compress () 
{
if [ -f $1 ]  ; then
   	case $1 in
   	*.tar.bz2)     tar $1    ;;
   	*.tar.gz)      tar $1    ;;
   	*.bz2)         bunzio2 $1 ;;
  	*.rar)         rar x $1 ;;
   	*.gz)          gunzip $1  ;;
   	*.tar)         tar $1     ;;
   	*.tbz2)        tar $1     ;;
   	*.tgz)         tar $1     ;;
   	*.zip)         zip $1   ;;
   	*.Z)            compress $1 ;;
	*.7z)          7z x $1      ;;
	*)             echo "'$1' cannot be compressed via ex()" ;;
   	esac
else  
    echo "'$1' is not a valid file"
fi


}


#RM() 
#{
#	if [ -f $1] ; then
#	    case $1 in
#		*.*)   rm -f $1   ;;
#		*)     rm -rf $1  ;;
#}


# source ~/.commacd.sh

################ ALIASES #########################
alias ls='exa -1l --icons'
alias grep='grep --colour=auto'
alias egrep='egrep --colour=auto'
alias fgrep='fgrep --colour=auto'
#alias cp="cp -i"                          # confirm before overwriting something
#alias df='df -h'                          # human-readable sizes
#alias free='free -m'                      # show sizes in MB
#alias np='nano -w PKGBUILD'
#alias more=less
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
alias e="$EDITOR"
alias se="sudo $EDITOR"
alias rmrf="rm -rf"
alias scp="scp -r"
alias systemctl="sudo systemctl"
# alias ascii="toilet -t -f 3d"
# alias future="toilet -t -f future"
# alias rusto="toilet -t -f rusto"
# alias rustofat="toilet -t -f rustofat"
alias untar='tar -xvzf'
alias myip="curl http://ipecho.net/plain; echo"
alias c="clear"
alias v="vim"
alias h="history"
alias ويب="$BROWSER"

###DNF ALIASES
alias install="sudo dnf install "
alias update="sudo dnf update "
alias remove="sudo dnf remove "
alias search="sudo dnf search "

alias py="python"
alias x="exit"
alias hg='history | grep $1'
# alias /="cd /"
alias hg='history | grep $1'
alias ..='cd ..'
alias ....="cd ../../"
alias ......="cd ../../../"
alias ~="cd ~/"
alias Downloads="cd ~/Downloads/"
alias Documents="cd ~/Documents/"
alias count='find . -type f | wc -l'
alias mnt="mount | awk -F' ' '{ printf \"%s\t%s\n\",\$1,\$3; }' | column -t | egrep ^/dev/ | sort"
alias grep='grep --color=auto'
alias mount='mount |column -t'
alias j='jobs -l'
alias ports='netstat -tulanp'
alias s="sudo "
alias reboot='sudo /sbin/reboot'
alias poweroff='sudo /sbin/poweroff'
alias shutdown='sudo /sbin/shutdown'
alias wget='wget -c'
alias start_docker='sudo systemctl start --now docker'
alias grep='grep --color=auto'

alias addup='git add -u'
alias addall='git add .'
alias branch='git branch'
alias checkout='git checkout'
alias clone='git clone'
alias commit='git commit -m'
alias fetch='git fetch'
alias pull='git pull origin'
alias push='git push origin'
alias stat='git status' # 'status' is protected name so using 'stat' instead
alias tag='git tag'
alias newtag='git tag -a'
alias yta-aac="yt-dlp --extract-audio --audio-format aac "
alias yta-best="yt-dlp --extract-audio --audio-format best "
alias yta-flac="yt-dlp --extract-audio --audio-format flac "
alias yta-m4a="yt-dlp --extract-audio --audio-format m4a "
alias yta-mp3="yt-dlp --extract-audio --audio-format mp3 "
alias yta-opus="yt-dlp --extract-audio --audio-format opus "
alias yta-vorbis="yt-dlp --extract-audio --audio-format vorbis "
alias yta-wav="yt-dlp --extract-audio --audio-format wav "
alias ytv-best="yt-dlp -f bestvideo+bestaudio "
#alias brightness="xrandr --output eDP-1 --brightness"
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"
alias tofish="sudo chsh $USER -s /bin/fish && echo 'Now log out.'"
alias topwsh='sudo chsh amro -s /usr/bin/pwsh && echo '\''Now log out.'\'
#alias vim="nvim"
alias vi="vim"
#alias icat="kitty +kitten icat"
alias disks='echo "╓───── m o u n t . p o i n t s"; \
			 echo "╙────────────────────────────────────── ─ ─ "; \
			 lsblk -a; echo ""; \
			 echo "╓───── d i s k . u s a g e";\
			 echo "╙────────────────────────────────────── ─ ─ "; \
			 df -h;'




## TTY dracula theme

if [ "$TERM" = "linux" ]; then
	printf %b '\e[40m' '\e[8]' # set default background to color 0 'dracula-bg'
	printf %b '\e[37m' '\e[8]' # set default foreground to color 7 'dracula-fg'
	printf %b '\e]P0282a36'    # redefine 'black'          as 'dracula-bg'
	printf %b '\e]P86272a4'    # redefine 'bright-black'   as 'dracula-comment'
	printf %b '\e]P1ff5555'    # redefine 'red'            as 'dracula-red'
	printf %b '\e]P9ff7777'    # redefine 'bright-red'     as '#ff7777'
	printf %b '\e]P250fa7b'    # redefine 'green'          as 'dracula-green'
	printf %b '\e]PA70fa9b'    # redefine 'bright-green'   as '#70fa9b'
	printf %b '\e]P3f1fa8c'    # redefine 'brown'          as 'dracula-yellow'
	printf %b '\e]PBffb86c'    # redefine 'bright-brown'   as 'dracula-orange'
	printf %b '\e]P4bd93f9'    # redefine 'blue'           as 'dracula-purple'
	printf %b '\e]PCcfa9ff'    # redefine 'bright-blue'    as '#cfa9ff'
	printf %b '\e]P5ff79c6'    # redefine 'magenta'        as 'dracula-pink'
	printf %b '\e]PDff88e8'    # redefine 'bright-magenta' as '#ff88e8'
	printf %b '\e]P68be9fd'    # redefine 'cyan'           as 'dracula-cyan'
	printf %b '\e]PE97e2ff'    # redefine 'bright-cyan'    as '#97e2ff'
	printf %b '\e]P7f8f8f2'    # redefine 'white'          as 'dracula-fg'
	printf %b '\e]PFffffff'    # redefine 'bright-white'   as '#ffffff'
	clear
fi
# If not running interactively, don't do anything
[[ $- != *i* ]] && return
source ~/.commacd.sh
complete -C /usr/local/bin/bit bit

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
source ~/.commacd.sh

eval "$(starship init bash)"


##add RTL support
printf "\e[?2501h"
printf "\e[2 k"



[ -f "/home/amro/.ghcup/env" ] && source "/home/amro/.ghcup/env" # ghcup-envalias dotconfig='/usr/bin/git --git-dir=/home/amro/.cfg/ --work-tree=/home/amro'
alias dotconfig='/usr/bin/git --git-dir=/home/amro/.cfg/ --work-tree=/home/amro'
