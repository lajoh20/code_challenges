Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:55d0:0:0:0:0 with SMTP id z16csp2529818ejp;
        Sun, 27 Sep 2020 08:54:01 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzZxyQlquUoXKK0Z6OUubny8qqbfDE4UCOmCCIzPJNiuyyILMb5fTBWyK5UV0EkouZ7mQpL
X-Received: by 2002:a37:9581:: with SMTP id x123mr8270583qkd.414.1601222041339;
        Sun, 27 Sep 2020 08:54:01 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1601222041; cv=none;
        d=google.com; s=arc-20160816;
        b=sA/g6Ht9+gMOBLli4cEo2R4xBh4sX6V+pJPSOXWZREkoSSNy2CJtxhTi+BxacQtfNw
         PJbpkPUHotZj1iAJIpyQ9RJs9u2Q97XubxcCowLyVQUT60Qf4gLF+268EZQx2P5hmdNr
         bg4jzHtBnCjwB9MPBcDDy+CKU5bVNQRvelNC5TPEIPgQ8fjfQbx/pmX+m83430hoeTy/
         HPUqECjkcRVqEXV+w5RRK0KJDPIqJW/oMc7LxNBexmXhp6tK+0lJGVZ3rqgo/rT+KaNf
         BbsPUnCwHBEtzs+wH3viwtyWkK9yfh1lKy3UmKWL1GITBFqYeTt0uuuBBjlXHYzVmonL
         8K5g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=smpqgothTEAbycexVGHgdMzmwXjfBzXHgsMdr7YQVEE=;
        b=0FSDBOEVoT2LbTi9AuRYHLSiAizU7BxrKKNgije2uX3Eso7PuIvVn7//qBTdsDgxWs
         AJVcrCPKiDJ5G0+ZQZNgjUyhFQku3TcNk+/mNeMzv780cQhNJ0NjFpIPNmdi9SFOa3ds
         r91acPuG27Ast06x/a/idG/i0C9CY9Ct2h6cS2vQD/jwVwQ3ekM6IVyPyQCtgettZZMd
         AhDYnmk/Gi4OLatgQNldpUExBRdYKzciHcew98EE2iGVR4804Gork2LzgsF7c3EOgjoP
         PHmsg2S8XcjYaDzv754tLRwcBA5M7aT5xicC+IZ7oGaEYU6k7vXgz2Hom6/qBvPUTISX
         W5Gw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=YdbBFEw2;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=h8qA8CQc;
       spf=pass (google.com: domain of 01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com
Return-Path: <01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id c4si3256384qtw.225.2020.09.27.08.54.00
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sun, 27 Sep 2020 08:54:01 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=YdbBFEw2;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=h8qA8CQc;
       spf=pass (google.com: domain of 01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1601222040;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=bCaD847px8uTTQ7XL7OHDpxLd7HBvSnGJoCWCP29jpc=;
	b=YdbBFEw2WmvhKjpb12zeSDVXRgbt3QSV7aEqWGeglabGy1NRgU5JZIozo3cdzU4+
	/b6YCaEFK0nGndPbtWE7qZJlQRZtLGyF4bL4UNGDLIWxWlBqHot7IMotXWZckbmwcLB
	BgXs8qIHPZhKfK21iyMAikMSLmfh0Kdm+SOYLDsc=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1601222040;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=bCaD847px8uTTQ7XL7OHDpxLd7HBvSnGJoCWCP29jpc=;
	b=h8qA8CQcWmE/kW5+OuYBvTuRh/7GHCB2hkNtXLE2qGbS32/7Wj7OA6S06XSoeq1U
	B0Facv3LaaAsXkcPuWZpDyrxMHPl5lZgC8VjcOFielBrmUr0Df5AMneSVY/0U8BsHMy
	PxkZmIoNkwP6jP526Qld62qvibUsjXlgpkkJblUA=
Content-Type: multipart/alternative;
 boundary="--_NmP-6db4413eb80e88b5-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #217 [Hard] 
Message-ID: <01000174d0455bc7-82e349b2-f0e6-42f4-a122-5407d0fc6784-000000@email.amazonses.com>
Date: Sun, 27 Sep 2020 15:54:00 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.09.27-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-6db4413eb80e88b5-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Oracle.

We say a number is sparse if there are =
no adjacent ones in its binary
representation. For example, 21 (10101) is =
sparse, but 22 (10110) is not. For a
given input N, find the smallest =
sparse number greater than or equal to N.

Do this in faster than O(N log =
N) time.


----------------------------------------------------------------=
----------------

Upgrade to premium
[https://www.dailycodingproblem.=
com/subscribe?email=3Dlewisjohnson1066334%40gmail.com]=20
and get in-depth solutions to every problem, including this one.=20

If you liked this problem, feel free to forward it along so they can =
subscribe
here [https://www.dailycodingproblem.com/]! As always, shoot us =
an email if
there's anything we can help with!


--------------------------=
------------------------------------------------------

Master algorithms together on Binary Search [https://binarysearch.io/?=
ref=3Ddcp].
Create a room, invite your friends, and race to finish the =
problem!


----------------------------------------------------------------=
----------------

No more? Snooze or unsubscribe
[https://dailycodingproble=
m.com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b=
8f89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-6db4413eb80e88b5-Part_1
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
    <title>Daily Coding Problem: Problem #217 [Hard]
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
Oracle.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">We say a number is sparse =
if there are no adjacent ones in its binary representation. For example, =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">21</code> (10101) is sparse, but <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">22</code> (10110) is not. For a given input <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">N</code>, find the smallest sparse number greater than=
 or equal to <code style=3D"font-family: monospace; margin: 0 2px; padding:=
 0 5px; white-space: nowrap; border: 1px solid #eaeaea; background-color: =
#f8f8f8; border-radius: 3px;">N</code>.</p>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Do this in faster than <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">O(N log N)</code> =
time.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;"><a=
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
----_NmP-6db4413eb80e88b5-Part_1--
