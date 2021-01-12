Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:55d0:0:0:0:0 with SMTP id z16csp551253ejp;
        Thu, 3 Sep 2020 09:00:55 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyFIDo4muOaAaVRJme8YZ/MA+JrzGTJWpEjYdWVSiSJwnIP4lDXIFvbp8nopAkzleOBEbex
X-Received: by 2002:a0c:ec02:: with SMTP id y2mr3661436qvo.140.1599148854926;
        Thu, 03 Sep 2020 09:00:54 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1599148854; cv=none;
        d=google.com; s=arc-20160816;
        b=a8X0dzql7wQjYRtF/5kyi5h6fAH2DUAQ0bapeF49L0EHUQGjRaMyJ0MaxnxUcLS2t9
         0i09gqkYABKMksYqAclWniF19Wm1pPvcILhEptslAtzHw8SUQVk4pEvBHmPlF7CR4SF4
         bHlMBhw78Hvz5rx38qERob0D4JvEwYOqVGATYwoKAbdNe/WQUeKeUtfETqpZbUi84QG1
         AX/Wbn6geWVf+nv+b51A59P16/bfkcHg3vSHybQgBnAQgMVnPSHb1/BCLruh74SL0qbh
         r6RCmoiA0xzNntyMa61B5eimZ0fBF28J5vvv5XoxwcZxDh6LQMG5zRr9Y2/mD3QdYD66
         e83Q==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=rc9qm6bv3rO7C8762PtkclINNe0qOX+u4Vq+CYZm3pg=;
        b=ZxAuTFp+gSL8vQGA3RhJfzJIMGeRq3qaBRnLxGKiFxJTMCE6S+oj7VlXf2sW/lTgiC
         KaeJ/UOfU21W6AyKtLb/SmLa2UokqR0+1nu+znctaJs3fnBR3vxV4fctYpdo+WSLuuAX
         vw/r0+PDgEcB4MeOtRmtV+indkKLNxb3NWHXPxtte6atkW1pvsHemF6DWNbrHZojGZJF
         Y7KiIYNYLXEH4sEW6HzIOBk40RLaQvy6sp3JW/MUHz4qi6fwuYfQedpbVNBd2uzKuvLS
         Yvx9xh3Qo9HKl3JlYIVYTHuPjVnaks0L0ixGbMvAlVcsP6j6FTFLqIN9UTp33HCBl5Lg
         NVpQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b="T1/u81/G";
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=j7II2MpW;
       spf=pass (google.com: domain of 0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com
Return-Path: <0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id f48si2206249qte.405.2020.09.03.09.00.54
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 03 Sep 2020 09:00:54 -0700 (PDT)
Received-SPF: pass (google.com: domain of 0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b="T1/u81/G";
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=j7II2MpW;
       spf=pass (google.com: domain of 0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1599148854;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=c7iOcbNueC2hslni1AAkc964hRMut+QgrArQfkjeTWY=;
	b=T1/u81/GdzbUnDjnJlOZVps7adzEb8zK88LCRyIOmcqWzveALR9GtTZdS5jKV01I
	o9iUvue5XANV95ApF90gWZ0Bjw5h9NnzszGGf619chyRutjRao9NjIuGPiN9jvvyhQ1
	jKilsW7zn6Vyo6cUcKzky4IhEsB234NdQM8xAtSM=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1599148854;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=c7iOcbNueC2hslni1AAkc964hRMut+QgrArQfkjeTWY=;
	b=j7II2MpW4JOekjlccchfvctBxVSMaHod0pJofJQ6oI6yr569RzcQVcZKXi69SPVi
	obUUey5KoXNk3Blw3y1wiSCsT52j7VK+luuhVp4WRZiBo1ctUmvuXnC6cN2n8mcbUQ2
	0z5fzRoynESfilp+Ko+MGa56B6BEkGuRz13Ma5P0=
Content-Type: multipart/alternative;
 boundary="--_NmP-16a988091e9eac1d-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #193 [Hard] 
Message-ID: <0100017454b30b1d-680d6d23-59a1-4bce-89d9-71c9111e24b5-000000@email.amazonses.com>
Date: Thu, 3 Sep 2020 16:00:54 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.09.03-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-16a988091e9eac1d-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Affirm.

Given a array of numbers representing =
the stock prices of a company in
chronological order, write a function that=
 calculates the maximum profit you
could have made from buying and selling =
that stock. You're also given a number=20
fee that represents a transaction=
 fee for each buy and sell transaction.

You must buy before you can sell =
the stock, but you can make as many
transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee =3D 2, you should return 9, =
since
you could buy the stock at 1 dollar, and sell at 8 dollars, and then =
buy it at 4
dollars and sell it at 10 dollars. Since we did two =
transactions, there is a 4
dollar fee, so we have 7 + 6 =3D 13 profit minus=
 4 dollars of fees.


-----------------------------------------------------=
---------------------------

Upgrade to premium
[https://www.=
dailycodingproblem.com/subscribe?email=3Dlewisjohnson1066334%40gmail.=
com]=20
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
----_NmP-16a988091e9eac1d-Part_1
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
    <title>Daily Coding Problem: Problem #193 [Hard]
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
Affirm.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a array of numbers =
representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made =
from buying
and selling that stock. You&#39;re also given a number <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">fee</code> that represents a transaction
fee for each buy and sell transaction.</p>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">You must buy before you can sell the stock, but you can make =
as many transactions as you like.</p>
<p style=3D"margin-top: 0; color: =
#555; font-size: 16px; line-height: 1.5em; text-align: left; font-family: =
Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For example, given [1, 3, 2, 8, 4, 10] and <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">fee =3D 2</code>, you should return 9, since you could=
 buy the stock
at 1 dollar, and sell at 8 dollars, and then buy it at 4 =
dollars and sell it at 10 dollars. Since
we did two transactions, there is =
a 4 dollar fee, so we have 7 + 6 =3D 13 profit minus 4 dollars of fees.</p>
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
----_NmP-16a988091e9eac1d-Part_1--
