## ***Developed by Vũ Quang Đại / <QuangDaiVQD@gmail.com>***
> [!Warning]
> Please respect copyright, I created this software without any cost or support. ***DO NOT STEAL THE CODE AND MAKE IT YOURS, WHILE EVERYTHING IS BUILT BY ME***. For example: edit ***Author & Developed by: Vu Quang Dai*** to your name, I know open source you can edit everything, but I want respect for the effort I put in.

*A tool to recover corrupted videos (MP4, MOV...) extracted from h264. I am developing independently, looking forward to receiving contributions from the community.
More references: [untrunc](https://github.com/anthwlock/untrunc), [recovery_mp4](https://slydiman.me/eng/mmedia/recover_mp4.htm)...etc
The goal is to learn & improve file repair techniques. Thanks!*

```You can contact me via gmail (email) to save the files you need. This will cost you a fee, thank you. If you have any problems or questions here => https://github.com/VQD-BSV-Official/BSV-VideoRepair/issues, I will reply as soon as possible.```



## Usage
Supports analysis of all video and audio formats <br>
Supported video formats: AVC/H.264 (avc1) <br>

VideoRepair - Early version: [click here](https://github.com/VQD-BSV/VideoRepairTool) <br>
DVFix - Download here for Windows [click here](https://github.com/VQD-BSV-Official/DVFix/releases)


Usage 1: <========> Deep File Analyze <========>
```
Step 1: DVFix.exe "good_file" --analyze
Step 2: DVFix.exe "bad_file" result.h264 --repair [option]
```
```
[option]: Samples Available
        --android  ❯  AVC     ~ 00 00 00 01
        --qt       ❯  MOV/AVC ~ 00 00 00 01
        --canon    ❯  XF-AVC  ~ 00 00 00 01
        --sony     ❯  XAVC    ~ 09 (10, 30, 50) 00 00
        --default  ❯  Use hex directly from the template file ~ 00 00 00 01 (Recommend)

```

Usage 2: <========> Ransomware File Analyze <========>
```
1 Step: DVFix.exe "bad_file" --ransom
```


> [!Note]
> * Using Python 3.13.5
> * Recommended to run on Windows, instead of Linux.
> * Good sample file. The file must be the same device or software. <br>
> The same parameters (Resolution, FPS, audio format).


> [!Important]
> **Donate**: [Do consider donating or buying us a coffee](https://paypal.me/BSVPay)
> ***Metamask**: 
