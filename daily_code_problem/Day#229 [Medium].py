Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:9984:0:0:0:0 with SMTP id af4csp1387117ejc;
        Fri, 9 Oct 2020 08:53:57 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJwzSK0OkBy7n/W4loB/kYjiIEAc3voSJ2tBknCIWp3WIIXdCk2loYJZV6CQ7Yzc6m4bQJeb
X-Received: by 2002:ac8:1199:: with SMTP id d25mr13997648qtj.260.1602258837657;
        Fri, 09 Oct 2020 08:53:57 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1602258837; cv=none;
        d=google.com; s=arc-20160816;
        b=RkOTqMRgEthjrLFBI9CDmMIiF+r9DatKtt2Nm3caRmSPEMkGBsIKrH/MgK8dXd8f7c
         PRONEzzQdQO+qf5J0G3j5sO4tIZ4/zle/EKYS8j41NxA81ZaA3oW6RhUEKbejxSXneQ7
         UbByZrxgANEo49S7oa3l79ybrqQwZO1XpKjhJ1g20vAZkG++Z4jD+etAHYPNWLgU5cFx
         x9ezDsyflgwpC9hOAOJoEXLfJZpMsI5Jt37Y1az8pGCyPq9I43IhG9qU3nAlb1PWAXv6
         7EnbbRb8Z9f3YyW8Y+Vf7Oe7HxwtqB/UI4e+joUuI+PJkpH3hkjpL0BF0oxZXzuj9alq
         LLvQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=jGQb6dnRIwVnppQF4U0C0pS5bZT1f98lITjXugDTjF8=;
        b=slxI/ytNI5i4PwkQng+zdOeOuUvKSElczn775XE6uG94TuM0IoOlOT0bqNOLo/452O
         oi376veZmTuYg4HgZVmrl444/+A7EGWdMkZnyryzQSq80GI87Dhw2qF2VoxEDiX1zsvQ
         tvf/heL7OgT1vm54Q3fIEHMLxbtxhKer7P65d2Jh2Xqfx0Q+nYm5LXSA+RyQeFe3P4zn
         rWDdeV2UQiSjDZ+d9SbtjHgnIJMwnMliAZZCZ+ub2rIwhgAMPrfw5SNCXJvn7BDIj5Du
         A9IQNn4I7jmwxyNPKzS3QlyFfegx55IMYUwH20Aaa+88DfV1nU0coUAxBDau1uSXsqQE
         43cQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=SiI+moBp;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=P99Jw3JT;
       spf=pass (google.com: domain of 010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com
Return-Path: <010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id o24si4734825qtl.352.2020.10.09.08.53.56
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 09 Oct 2020 08:53:57 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=SiI+moBp;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=P99Jw3JT;
       spf=pass (google.com: domain of 010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1602258836;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=xn2D8y/y70WlUCVBs2nCclIVsy4KzKEzbwUA7jNoTjg=;
	b=SiI+moBpSn5SJYL9SzpEUdSCnfxAYNJmRSgFbaTR3wMhqjDfroYDAfalkLhGYBlM
	8Cp5LvqUvKJFkW2anz6j9i9lBZEdbbl0y9PHqVMd/YIxS4qKnZD3KjUvulshr4ozbyG
	TSj6WnqhthBaf2g4r9dE6QrC8DHFkApYpMDTHFh0=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1602258836;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=xn2D8y/y70WlUCVBs2nCclIVsy4KzKEzbwUA7jNoTjg=;
	b=P99Jw3JTh7nOAN9Y9s7lXMa7fABoBJKckdk52O0Ws8M+HUqBVxNFU5U8CatOSgr2
	6ZKmFdutBiSa+TMCbbWRuRRIjNY9OTCVCFiNWueNGcdNqUqnSt+7ob88fqAOG1KgdJE
	6MhBl65JkN9eI/I5YfJSS/8ZIjXXJhdGLN2yGrM4=
Content-Type: multipart/alternative;
 boundary="--_NmP-8a677039bb4a7941-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #229 [Medium] 
Message-ID: <010001750e119bae-fd66b024-36e8-4e09-8073-55e261acb00d-000000@email.amazonses.com>
Date: Fri, 9 Oct 2020 15:53:56 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.10.09-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-8a677039bb4a7941-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Flipkart.

Snakes and Ladders [https://en.=
wikipedia.org/wiki/Snakes_and_Ladders] is a game
played on a 10 x 10 board,=
 the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move forward a number of
spaces equal to the result. If they land on a square that represents a =
snake or
ladder, they will be transported ahead or behind, respectively, to=
 a new square.

Find the smallest number of turns it takes to play snakes =
and ladders.

For convenience, here are the squares representing snakes and=
 ladders, and their
outcomes:

snakes =3D {16: 6, 48: 26, 49: 11, 56: 53, =
62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders =3D {1: 38, 4: 14, =
9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}



---------------------------------------------------------------------------=
-----

Upgrade to premium
[https://www.dailycodingproblem.com/subscribe?=
email=3Dlewisjohnson1066334%40gmail.com]=20
and get in-depth solutions to =
every problem, including this one.=20

If you liked this problem, feel free=
 to forward it along so they can subscribe
here [https://www.=
dailycodingproblem.com/]! As always, shoot us an email if
there's anything we can help with!


--------------------------------------=
------------------------------------------

Master algorithms together on =
Binary Search [https://binarysearch.io/?ref=3Ddcp].
Create a room, invite your friends, and race to finish the problem!


---------------------------------------------------------------------------=
-----

No more? Snooze or unsubscribe
[https://dailycodingproblem.=
com/unsubscribe?unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f=
89172d630e6f6de658c7d6d6b960ec]
.
----_NmP-8a677039bb4a7941-Part_1
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
    <title>Daily Coding Problem: Problem #229 [Medium]
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
Flipkart.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;"><a href=3D"https://en.=
wikipedia.org/wiki/Snakes_and_Ladders" style=3D"color: #3869D4; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Snakes and Ladders</a> is a game played on a <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">10 x 10</code> board, the goal of which is get from =
square <code style=3D"font-family: monospace; margin: 0 2px; padding: 0 =
5px; white-space: nowrap; border: 1px solid #eaeaea; background-color: =
#f8f8f8; border-radius: 3px;">1</code> to square <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">100</code>. On each turn players will roll a six-sided=
 die and move forward a number of spaces equal to the result. If they land =
on a square that represents a snake or ladder, they will be transported =
ahead or behind, respectively, to a new square.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Find the smallest number of turns it =
takes to play snakes and ladders.</p>
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For convenience, here are the squares representing snakes and =
ladders, and their outcomes:</p>
<pre style=3D"background-color: #f8f8f8; =
border: 1px solid #cccccc; font-size: 13px; line-height: 19px; overflow: =
auto; padding: 6px 10px; border-radius: 3px;"><code style=3D"border-radius:=
 3px; font-family: monospace; margin: 0; padding: 0; white-space: pre; =
background: transparent; background-color: transparent; border: =
none;">snakes =3D {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, =
93: 73, 95: 75, 98: 78}
ladders =3D {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, =
36: 44, 51: 67, 71: 91, 80: 100}
</code></pre><hr style=3D"font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;"><a href=3D"https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.com" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Upgrade to premium</a> and get =
in-depth solutions to every problem, including this one. </p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">If you liked this problem, feel free =
to forward it along so they can <a href=3D"https://www.dailycodingproblem.=
com/" style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">subscribe here</a>! As =
always, shoot us an email if there&#39;s anything we can help with!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Master =
algorithms together on <a href=3D"https://binarysearch.io/?ref=3Ddcp" =
style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Binary Search</a>. Create a room, =
invite your friends, and race to finish the problem!</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">
<p style=3D"margin-top: 0; color: #555; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box; font-size: 0.7em;">
  No more? <a href=3D"https://dailycodingproblem.com/unsubscribe?=
unsubscribeKey=3D15bb4345a533060b01c0f75abaabcc917938df8b8f89172d630e6f6de6=
58c7d6d6b960ec" style=3D"color: #3869D4; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">Snooze or =
unsubscribe</a>.
</p>

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
						<!-- Email Footer -->
						<tr>
              <td =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
                <table =
class=3D"email-footer" align=3D"center" width=3D"570" cellpadding=3D"0" =
cellspacing=3D"0" style=3D"font-family: Arial, 'Helvetica Neue', Helvetica,=
 sans-serif; box-sizing: border-box; width: 570px; margin: 0 auto; padding:=
 0; -premailer-width: 570px; -premailer-cellpadding: 0; =
-premailer-cellspacing: 0; text-align: center;">
                  <tr>
                    <td class=3D"content-cell" align=3D"center" =
style=3D"word-break: break-word; font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box; padding: 35px;">
                      <p class=3D"sub align-center" style=3D"margin-top: 0;=
 line-height: 1.5em; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box; text-align: center; color: #AEAEAE; =
font-size: 12px;">&copy; 2019 Daily Coding Problem. All rights reserved.=
</p>
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
----_NmP-8a677039bb4a7941-Part_1--
