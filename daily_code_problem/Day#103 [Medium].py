Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:86c1:0:0:0:0 with SMTP id j1csp2838907ejy;
        Fri, 5 Jun 2020 08:47:01 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJxDqjMFhzXRLVkkoUTBS8S7hPthFol/HbLZ5XDR4mOVcJUMMQtZCUXzCN06U0uXl6hMC5ch
X-Received: by 2002:a37:e85:: with SMTP id 127mr10266363qko.178.1591372021321;
        Fri, 05 Jun 2020 08:47:01 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1591372021; cv=none;
        d=google.com; s=arc-20160816;
        b=yquNrpJTcZXQwTwi3e2X0MCV3QIwctGr0XBIVYiuWCkzF5kO5Go1oFEpZHQ8YckYSH
         7gC2MPTG3mZxEb+1/tGSPNsX+qnrJF1SulOwyZ31L9bk+SNWstACQRF9v1ibpzXBU72t
         SMj85RXwPNQbsNPdEkb3/PWdCAMw9Hd1R62P96xkAAdvdAQ1EKMX9FYRMjkg8IJlvdlG
         hmoF0ENzdfsJBvZEFLENKlQCF5237N32Tiu6dEPX82aBle6Khq+jUAr/0U7qllOWCjAt
         RglJkNKinPFd7MlY7sXGUvdoFWxnNfDdPrm3MitkXSz5XIDd7VogQa5Rti8PyLIqKSqh
         5tFw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=qxcD81HitL0ZeMQt6r1Qjno4x7hurRgBDp5Zz7GbMC0=;
        b=wcNw6dHoomDtnUkKGqPzad8Zcc8LLz0LkBUOgIUkqhHvWfft6M7RdKmS6MQLeYEEHR
         oDDMvRB37ex/llEXH3nTZEKPEsoTYbvnb+Yb/bXP+EEJiteYPLicwKHTT7cfwnOmBar6
         4sHREKlFoBn/6v0NxD1r1zIsICdrHUxrbrm2QxxciytfhnwbpgAktq/bN90D6Vf1yyj8
         WW881i49mqHkrQZOngehIzCEd8HQLNldesS8pTAB1rbfe7qbOe4Np4c4W4xN+/gozBMJ
         I9SVX/ZLElv7B+GC25yv/toext/GS8TTqHfKG2fq3Hk3j9tYQAmzXdBm17TKnL+hyzmD
         gmbA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=lpcgYZfs;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Dn9CveKH;
       spf=pass (google.com: domain of 010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com
Return-Path: <010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id w27si59202qtb.244.2020.06.05.08.47.01
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 05 Jun 2020 08:47:01 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=lpcgYZfs;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=Dn9CveKH;
       spf=pass (google.com: domain of 010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1591372020;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=WyaNw05ZsVpre71HCmeQAF6a/rP+SGlG7hf7tb3S7q4=;
	b=lpcgYZfsReGpX3k9gvKHOLv4Ap3fAZm2PZ+c/3p/ziJ71gkvqlV5AuMeLFj7ZM3o
	SpFI6R1b6LDQrgaSrx0Exp18DwQMDOpBEVkdMmAtq8UngBU3eN8pPbFSZlZvx2TFSh7
	BSun9y339ZqGkltKDyetOEN4UhzL2tRsxr4K6Pms=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1591372020;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=WyaNw05ZsVpre71HCmeQAF6a/rP+SGlG7hf7tb3S7q4=;
	b=Dn9CveKHDM1Xrh5+wpfKIsJbYFQOgVRPsnlb1bN+bZ2q7IcP3OM5zL/19suRdqtC
	xIfi/zTKu/SvOP9yQe/cbuZclCfvQJJq6uMSyKGGfL3BpAMqyRlGCWd8e3b7To2pQ4c
	P4xG7Np+8frVS1z04aXQYQrQ0qIqPtJ+xVXSmhtg=
Content-Type: multipart/alternative;
 boundary="--_NmP-0c554577338f06f4-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #103 [Medium] 
Message-ID: <010001728529fc0f-d6698d03-e414-4fdf-8c4c-be54e464b228-000000@email.amazonses.com>
Date: Fri, 5 Jun 2020 15:47:00 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.05-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-0c554577338f06f4-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a string and a set of characters, =
return the shortest substring containing
all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, =
i},
you should return "aeci".

If there is no substring containing all the =
characters in the set, return null.


-------------------------------------=
-------------------------------------------

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%4=
0gmail.com]=20
and get in-depth solutions to every problem, including this =
one.=20

If you liked this problem, feel free to forward it along so they =
can subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot =
us an email if
there's anything we can help with!


---------------------------------------------------------------------------=
-----

Master algorithms together on Binary Search [https://binarysearch.=
io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-0c554577338f06f4-Part_1
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.=
w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=3D"http://www.w3=
.org/1999/xhtml">
  <head>
    <meta name=3D"viewport" =
content=3D"width=3Ddevice-width, initial-scale=3D1.0">
    <meta http-equiv=3D"Content-Type" content=3D"text/html; =
charset=3DUTF-8">
    <title>Daily Coding Problem: Problem #103 [Medium]
</title>
    <style type=3D"text/css" rel=3D"stylesheet" media=3D"all">
@media only screen and (max-width: 600px) {
  .email-body_inner,
.email-footer {
    width: 100% !important;
  }
}
@media only screen and =
(max-width: 500px) {
  .button {
    width: 100% !important;
  }
}
</style>
  </head>
  <body style=3D"height: 100%; margin: 0; line-height: 1.4; =
background-color: #F2F4F6; color: #74787E; -webkit-text-size-adjust: none; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box; width: 100%;">
    <table class=3D"email-wrapper" =
width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; background-color: =
#F2F4F6;" bgcolor=3D"#F2F4F6">
      <tr>
        <td align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
          <table =
class=3D"email-content" width=3D"100%" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 100%; margin: 0; padding: 0; =
-premailer-width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: =
0;">
            <table class=3D"email-head_inner" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0;">
              <tr>
                <td class=3D"email-masthead" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 25px 35px; height: 30px; vertical-align: =
middle; border-collapse: collapse;" height=3D"30" valign=3D"middle">
                  <a href=3D"https://www.dailycodingproblem.com/" =
class=3D"email-masthead_logo_link" style=3D"color: #3869D4; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; vertical-align: middle; text-decoration: none; =
padding: 0; margin: 0; display: inline-block;">
                    <img =
class=3D"email-masthead_logo" src=3D"https://www.dailycodingproblem.=
com/static/icon-round.png" width=3D"30" height=3D"30" style=3D"font-family:=
 Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 30px; height: 30px; border: 0; vertical-align: middle;">
                  </a>
                  <a href=3D"https://www.=
dailycodingproblem.com/" class=3D"email-masthead_link" style=3D"color: =
#3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; height: 30px; vertical-align: middle; padding-left:=
 6px; text-decoration: none;">
                    <span =
class=3D"email-masthead_name" style=3D"font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box; font-size: 14px; =
font-weight: bold; color: #343434; text-decoration: none; text-shadow: 0 =
1px 0 white; height: 50px;">Daily Coding Problem</span>
                  </a>
                </td>
              </tr>
            </table>
            <!-- Email Body -->
            <tr>
              <td class=3D"email-body" width=3D"100%" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; width: =
100%; margin: 0; padding: 0; -premailer-width: 100%; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; border-top: 1px solid=
 #EDEFF2; border-bottom: 1px solid #EDEFF2; background-color: #FFFFFF;" =
bgcolor=3D"#FFFFFF">
                <table class=3D"email-body_inner" =
align=3D"center" width=3D"570" cellpadding=3D"0" cellspacing=3D"0" =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; width: 570px; margin: 0 auto; padding: 0; =
-premailer-width: 570px; -premailer-cellpadding: 0; -premailer-cellspacing:=
 0; background-color: #FFFFFF;" bgcolor=3D"#FFFFFF">
                  <!-- Body content -->
                  <tr>
                    <td class=3D"content-cell" style=3D"word-break: =
break-word; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; padding: 35px;">
											<p style=3D"margin-top:=
 0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Good morning! Here&#39;s your coding interview problem for =
today.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">This problem was asked by =
Square.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a string and a set =
of characters, return the shortest substring containing all the characters =
in the set.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">For example, given the =
string &quot;figehaeci&quot; and the set of characters {a, e, i}, you =
should return &quot;aeci&quot;.</p>
<p style=3D"margin-top: 0; color: #555;=
 font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">If there=
 is no substring containing all the characters in the set, return null.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><a =
href=3D"https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Upgrade to premium</a> and get in-depth solutions to every =
problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">If you =
liked this problem, feel free to forward it along so they can <a =
href=3D"https://www.dailycodingproblem.com/" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">subscribe here</a>! As always, shoot us an email if =
there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial,=
 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Master algorithms together on <a =
href=3D"https://binarysearch.io/?ref=3Ddcp" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Binary Search</a>. Create a room, invite your friends, and =
race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica=
 Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; line-height: 1.5em; text-align: =
left; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box; font-size: 0.7em;">
  No more? <a =
href=3D"https://dailycodingproblem.com/unsubscribe?unsubscribeKey=3D15bb434=
5a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de658c7d6d6b960ec" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Snooze or unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td style=3D"word-break: break-word; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
                <table class=3D"email-footer" align=3D"center" =
width=3D"570" cellpadding=3D"0" cellspacing=3D"0" style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; =
width: 570px; margin: 0 auto; padding: 0; -premailer-width: 570px; =
-premailer-cellpadding: 0; -premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" =
align=3D"center" style=3D"word-break: break-word; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box; padding: =
35px;">
                      <p class=3D"sub align-center" =
style=3D"margin-top: 0; line-height: 1.5em; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box; text-align: center; =
color: #AEAEAE; font-size: 12px;">&copy; 2019 Daily Coding Problem. All =
rights reserved.</p>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
----_NmP-0c554577338f06f4-Part_1--
