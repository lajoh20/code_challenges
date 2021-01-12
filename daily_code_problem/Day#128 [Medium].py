Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp4299978ejc;
        Tue, 30 Jun 2020 08:48:49 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJzq2LiAz9uZnqsGL4TrfNruNZgBUUMRAwOHnBMaFrsfarEQXg4XYrEIXLEuTg1hbVqLFbhp
X-Received: by 2002:ac8:f6f:: with SMTP id l44mr19961369qtk.4.1593532129761;
        Tue, 30 Jun 2020 08:48:49 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1593532129; cv=none;
        d=google.com; s=arc-20160816;
        b=SCBEsb67bndwelmTBpTvWe3uwfOgbvjjoRIL1zdKcJHOw0p+raxmj3VyePN8+oNAAR
         ExJDX1gp4XSjeVi4TvbQj2g2keMDQ/vKNyTqPB/An5I518tBw1wGCfSREeachyZqKjGA
         Pf7G6n0eSAz1SkdEGia4NVH0pksbbEApMGvB5PhA3SwDXK93VujqptKBWkTumMlz+xD9
         5cBPys3EbKiFx+wWWIsuVLZBnCl1cMeTWnSbIliN8I9k6wZKVEsxbXo9TFKU3EXZopiu
         JjHDswDR4nijsiKldIkOYYbD1wd2U26NemLMCY3ToqLrxzjTaqYEH/3wP+y7ayHxW8qJ
         zZpg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=8RgkeyQZRWaIFAfiY0PpEZz6zsBH3L2cNG4ig9qEQxU=;
        b=QoaBgT/r7gwgVZKuYx4GuK9CwI/1+ii5nOQkHQyRJpnoWOO3k5ygjmg/IB3lN/Dt3Z
         2Ig3aPKZLeLNgT6bUzc7L2iRpbTZW5J5CrU2XcAWuLjJmJTCkw8adAJuapX82jHnqVR4
         OEVnrC8yXEQUVYJDXlut72PAOtSaMADxmv03XSfH7TuyycWjuwLK2leKLOcxZXFgw6dR
         LpXPQ5dzNqQCRPYs96yPqS9f79GNxppsKtb+lO1Igzf0/xDZqxuyhCJmwWyqST8AAxBO
         1bbsH3KRns8QDo8UpTuH1ECBtz7GtmquwmAEnRKBI0yF9L+zPmWMtSObBkb5basXyTWz
         zjgw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Qr+IAaau;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=PUysFvzQ;
       spf=pass (google.com: domain of 0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com
Return-Path: <0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id g11si2027447qtc.296.2020.06.30.08.48.49
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Tue, 30 Jun 2020 08:48:49 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=Qr+IAaau;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=PUysFvzQ;
       spf=pass (google.com: domain of 0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1593532129;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=HEf64rWsSEcY1eRN1obFuC+ih7AO5jRI2CIcQpqmxcE=;
	b=Qr+IAaauVOcOQnaAEwsXN842JiUhy/Dr/PYn+qrkNZiB+YBDKgNSBc4KTTXaBSSx
	acPZmTL5nQCwvlQf1/b9MAGU59HdZQsoURL/Rl0qCmn2El7DimOo0U9CiCWdDGPMqof
	cuwe3PKvuy5RuQGvy5kWZBRr3vGbwLuGO/DPDKj0=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1593532129;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=HEf64rWsSEcY1eRN1obFuC+ih7AO5jRI2CIcQpqmxcE=;
	b=PUysFvzQi7fJeG9MQV9RNljc6qL+NMRKVrh7kmNF1SgMF1WEyZZvE6867YVX0uUF
	MAT5h+fXLVVOHEyrsdBoYdocFOWEWTKJmFoe9szvSzWaaTsSlOfPdWJHa+rJWe7YIsv
	dj8PR4XMctXL/0VIhARsBXb16NvuRIfA+RtrKxE8=
Content-Type: multipart/alternative;
 boundary="--_NmP-b189ac2bee04dcb0-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #128 [Medium] 
Message-ID: <0100017305ea9ff3-07afa9ac-db03-4609-abeb-4df651dd777b-000000@email.amazonses.com>
Date: Tue, 30 Jun 2020 15:48:49 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.30-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-b189ac2bee04dcb0-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

The Tower of Hanoi is a puzzle game with three rods and n disks, each a
different size.

All the disks start off on the first rod in a stack. They =
are ordered by size,
with the largest disk on the bottom and the smallest =
one at the top.

The goal of this puzzle is to move all the disks from the =
first rod to the last
rod while following these rules:

 * You can only move one disk at a time.
 * A move consists of taking the =
uppermost disk from one of the stacks and
   placing it on top of another =
stack.
 * You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the =
Tower
of Hanoi. You should assume that the rods are numbered, with the =
first rod being
1, the second (auxiliary) rod being 2, and the last (goal) =
rod being 3.

For example, with n =3D 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3



------------------------------------------------------------=
--------------------

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
----_NmP-b189ac2bee04dcb0-Part_1
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
    <title>Daily Coding Problem: Problem #128 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">The Tower of Hanoi is a =
puzzle game with three rods and n disks, each a different size.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">All the disks start off on the first =
rod in a stack. They are ordered by size, with the
largest disk on the =
bottom and the smallest one at the top.</p>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">The goal of this puzzle is to move all the disks from the =
first rod to the last rod while
following these rules:</p>
<ul style=3D"text-align: left; color: #555; font-size: 16px; line-height: 1=
.5em; padding-left: 24px; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">You can =
only move one disk at a time.</li>
<li style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">A move =
consists of taking the uppermost disk from one of the stacks and placing it=
 on top of another stack.</li>
<li style=3D"font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">You cannot place a =
larger disk on top of a smaller disk.</li>
</ul>
<p style=3D"margin-top: 0;=
 color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Write a function that prints out all the steps necessary to =
complete the Tower of Hanoi. You should
assume that the rods are numbered, =
with the first rod being 1, the second (auxiliary) rod being 2,
and the last (goal) rod being 3.</p>
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For example, with n =3D 3, we can do this in 7 moves:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
</code></pre><hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, =
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
----_NmP-b189ac2bee04dcb0-Part_1--
