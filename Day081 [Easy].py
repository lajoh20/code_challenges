Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1dd1:0:0:0:0 with SMTP id v17csp1517644ejh;
        Thu, 14 May 2020 08:42:21 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyvrD17lM3uJhN4ZXRKjuhVVLi+rgPVscjMpWYcNCJTeV+ew00gY8VxMyFYKctC/hryS/mj
X-Received: by 2002:a0c:df02:: with SMTP id g2mr5322699qvl.115.1589470940052;
        Thu, 14 May 2020 08:42:20 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1589470940; cv=none;
        d=google.com; s=arc-20160816;
        b=tN7uwxtWvbBDt0CJ3jIgTHkVOlnSuWNZM+94k2e+9kqzAfGoW4pWm0gdZbjqVYgMqy
         Y8MLylJ4uHY79L3FdmZvafpjrNLG4TMw4DPPHRm7M2+jR5LUI2YYSoJ91FLTMVldJBCN
         2feqXlHt2ND+UkXIS+Td689otqEX8map1JroFkVj4t3G8wZ4WBquYY8cj8g1HQ8Ql0S7
         h61YOw2g8cBYUDY18RYstKraWI4Eax2GsDJoDQtEiA9YozxXAD5KKvhBdID+is9OsSmt
         GMmESt600Cuc7lGhdMWO3s7ljop+Lq58k589lzj25qKmromyVOqjQXVL4Kb92T5zeTVf
         WzjA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=o/4GWneGbaBBg5piZW+BAp2P9732nEEdxB4+XxU3WaE=;
        b=gAWks//PVW7i/8Mpu8JSGgjYanCGDEoKGsAkhml1Q86Ycru9I1yZ/ptA2htEXrt7Qy
         y51j0Edlfd0iG3PbLGI2j4dxQincRs2/sNmtPp5VgPBiYQ6y7Vcqk/8SnfbGh4y92Bp/
         A9ytWbCDxDGQjP3gdnC4q6JGxsZhFMDvSbJkbRFhtXoNSg6qiOndfPNikjSXlQtftNZP
         9WyvtYxrt8sE10N7SnqLEvy1wVA2ivKQ8w5X/1Mm42zNJxRIjsuYUJBJhbcAH3w5htML
         wRHYPtqFvoHTZXUdxF1SOIhMgZL9zmSHR9GshNod/XFyaAFYSuXW3EVxXTptr4Bi2VA7
         lM5A==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=XDcIRC2a;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=G+s3BMjr;
       spf=pass (google.com: domain of 0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com
Return-Path: <0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id o143si1652295qke.14.2020.05.14.08.42.19
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 14 May 2020 08:42:20 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=XDcIRC2a;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=G+s3BMjr;
       spf=pass (google.com: domain of 0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1589470939;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=cNkNaTFn9fvjHhEKEJ3AfCyBvM/+Eb4qLzl1eHCyFyE=;
	b=XDcIRC2aOIa5oUeJe3Z7Bie9ePK0PY2Fy1GuNZU+PlCYig5rUo7sljD2uz/hPrXG
	aRv/zedbdxodvIXjMWYIoRCRoW2qGmY5rpu4BzkM2BD8bAzLz0p/5mJei6puo7BVIwF
	ksRy3REit2bNH5LYe3v5L62sUJWOpFFiWidyjupc=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1589470939;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=cNkNaTFn9fvjHhEKEJ3AfCyBvM/+Eb4qLzl1eHCyFyE=;
	b=G+s3BMjrAvoRUELcu6jvRvaIyBu2BrCSUf9PgZV2TDr42wLrgdkkNATQWuEtpmLj
	Tusx/65Gjy+UTWHHPeHJIZ+h2S8FSm8kGxAabVbG5KeGyIzzCG+U/rTIfLEBiGxi3Ts
	V/cMS6Dq0O8NgqeT77TlUX7dJmmprGsYJPm5NsUo=
Content-Type: multipart/alternative;
 boundary="--_NmP-265ba9ce8e840516-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #81 [Easy] 
Message-ID: <0100017213d9c8d2-0a761e6c-f477-4a79-9ce5-58b6f378b430-000000@email.amazonses.com>
Date: Thu, 14 May 2020 15:42:19 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.05.14-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-265ba9ce8e840516-Part_1
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

Given a mapping of digits to letters (as =
in a phone number), and a digit string,
return all possible letters the =
number could represent. You can assume each
valid number in the mapping is =
a single digit.

For example if {=E2=80=9C2=E2=80=9D: [=E2=80=9Ca=E2=80=9D,=
 =E2=80=9Cb=E2=80=9D, =E2=80=9Cc=E2=80=9D], 3: [=E2=80=9Cd=E2=80=9D, =
=E2=80=9Ce=E2=80=9D, =E2=80=9Cf=E2=80=9D], =E2=80=A6} then =
=E2=80=9C23=E2=80=9D should
return [=E2=80=9Cad=E2=80=9D, =
=E2=80=9Cae=E2=80=9D, =E2=80=9Caf=E2=80=9D, =E2=80=9Cbd=E2=80=9D, =
=E2=80=9Cbe=E2=80=9D, =E2=80=9Cbf=E2=80=9D, =E2=80=9Ccd=E2=80=9D, =
=E2=80=9Cce=E2=80=9D, =E2=80=9Ccf"].


------------------------------------=
--------------------------------------------

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
----_NmP-265ba9ce8e840516-Part_1
Content-Type: text/html; charset=utf-8
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
    <title>Daily Coding Problem: Problem #81 [Easy]
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
Yelp.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a mapping of digits =
to letters (as in a phone number), and a digit string, return all possible =
letters the number could represent.
You can assume each valid number in the=
 mapping is a single digit.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example if {=E2=80=9C2=E2=80=9D: [=E2=80=9Ca=E2=80=9D, =E2=80=9Cb=E2=80=9D,=
 =E2=80=9Cc=E2=80=9D], 3: [=E2=80=9Cd=E2=80=9D, =E2=80=9Ce=E2=80=9D, =
=E2=80=9Cf=E2=80=9D], =E2=80=A6} then =E2=80=9C23=E2=80=9D should return =
[=E2=80=9Cad=E2=80=9D, =E2=80=9Cae=E2=80=9D, =E2=80=9Caf=E2=80=9D, =
=E2=80=9Cbd=E2=80=9D, =E2=80=9Cbe=E2=80=9D, =E2=80=9Cbf=E2=80=9D, =
=E2=80=9Ccd=E2=80=9D, =E2=80=9Cce=E2=80=9D, =E2=80=9Ccf&quot;].</p>
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
----_NmP-265ba9ce8e840516-Part_1--
