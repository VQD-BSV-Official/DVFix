## ***Developed by Vũ Quang Đại / <BSVRecovery.vn@gmail.com>***
> [!Warning]
> Please respect copyright, I created this software without any cost or support. ***DO NOT STEAL THE CODE AND MAKE IT YOURS, WHILE EVERYTHING IS BUILT BY ME***. For example: edit ***Author & Developed by: Vu Quang Dai*** to your name, I know open source you can edit everything, but I want respect for the effort I put in.

*A tool to recover corrupted videos (MP4, MOV...) extracted from h264. I am developing independently, looking forward to receiving contributions from the community.
More references: [untrunc](https://github.com/anthwlock/untrunc), [recovery_mp4](https://slydiman.me/eng/mmedia/recover_mp4.htm)...etc
The goal is to learn & improve file repair techniques. Thanks!*

```You can contact me via gmail (email) to save the files you need. This will cost you a fee, thank you. If you have any problems or questions here => https://github.com/VQD-BSV-Official/BSV-VideoRepair/issues, I will reply as soon as possible.```



## Usage
Usage1: <========> Deep File Analyze <========>
```
Step 1: DVFix.exe "good_file.mp4" --analyze
```
```
Step 2: DVFix.exe "bad_file.mp4" result.h264 --repair [option]
```
```
[option]: Samples Available <br>
        --canon    ❯  EOS SX, 80D, 90D <br>
        --default  ❯  Use hex directly from the template file
```

Usage1: <========> Ransomware File Analyze <========>
```
S1: DVFix.exe [bad_file_path]  --ransom
```


> [!Note]
> * Using Python 3.12.4 or > Python 3.9
> * Recommended to run on Windows, instead of Linux.
> * Good sample file. The file must be the same device or software. <br>
> The same parameters (Resolution, FPS, audio format).


> [!Important]
> **Donate**: [Do consider donating or buying us a coffee](https://paypal.me/BSVPay)
