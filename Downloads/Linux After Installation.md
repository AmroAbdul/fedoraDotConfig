# After Linux Installation
**this are some stuff that can be done after installing a Linux distro, currently I'm using Arch Linux so somethings can be different in Other distros**
**هذا بعض ما يخصني من الإعدادات بعد تنصيب توزيعة أرتش لينكس, هذا لأنني أستخدمها في الوقت الراهن ولذا بعض الإعدادات قد تختلف في توزيعات آخرى**

## add keyboard layouts with a key shortcut 
## إضافة إعدادات لغات لوحة المفاتيح مع إعداد اختصار للتحويل بين اللغات
``

## fix hardware clock sync in Linux disto & Windows 
## إصلاح مشكلة تزامن الوقت بين لينكس وويندوز


## install required packages 
## تنصيب الحزم المطلوبة
*for me:*
*هذا ما أحتاجه من الحزم*
`qtile rofi rofi-emoji ntfs-3g alacritty vim neovim librewolf cbatticon volctl emacs git github-cli php composer nodejs npm python-pip postgresql qemu-full pgadmin4 postgis qgis google-earth telegram-desktop thunar gparted brave-bin base-devel paru exa bat .....`

*and other packages can be installed*
*هناك بعض الحزم الآخرى التي يمكن تنصيبها بطرق آخرى*
`starship doomemacs sysz `



## edit pacman.conf (I use Arch BTW) 
## تعديل ملف  pacman.conf

## edit sudoers 
## sudoers تعديل 

## services to be enables
`systemctl enable libvirt`

## add NTFS partitions to /etc/fstab
*note: this needs the ntfs-3g driver to be installed
first get the partition [UUID] using this command
`sudo blkid`
then add this line to the end of /etc/fstab using any text editor you wish (nano,vim,emac)


you can mount it wherever you want ([MOUNTDIR]) and you need to get USERID and GROUPID you can use these commands
`id -u`
`id -g`

`#using vim`
`sudo vim /etc/fstab`
`UUID="[UUID]" [MOUNTDIR] ntfs-3g uid=USERID,gid=GROUPID,dmask=022,fmask=133 0 0`

### example:
`UUID=7C266B3C266AF694      /Windows    ntfs-3g uid=1000,gid=1000,dmask=022,fmask=133 0 0`

## manage dot files using git bare init 
##  git إدارة والحفاظ على ملفات النقاط أو ملفات إعدادات التوزيعة باستخدام مدير الإصدارات الشهير






# fix boot problems


## changes needed to be done in Windows
**open cmd.exe and run the following**
``


<style>
    h1 {
        display:block;
        text-align:center;
    }
    h2 {
        display:flex;
        justify-content:center;
    }
</style>