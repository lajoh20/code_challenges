Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:4589:b029:b0:a332:2bfe with SMTP id s9csp2202495lkv;
        Fri, 18 Dec 2020 09:03:33 -0800 (PST)
X-Google-Smtp-Source: ABdhPJyAby//664n4GnBw8B+279Rsex52gAqytMAmRs9e36d2M4lIGOK1veAW6ysu/XjA0gYltwo
X-Received: by 2002:a37:a80f:: with SMTP id r15mr5620474qke.289.1608311013447;
        Fri, 18 Dec 2020 09:03:33 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1608311013; cv=none;
        d=google.com; s=arc-20160816;
        b=oLQa11Vvbq9i4O/NnKfh1LyvkqNAALxhR4S2kbhGXum9h7EdaCiTjW46g96c1PA7S6
         UDPWwB7W0Pwo5GXWklL2RrNA/80ji9GyYUK2eiHoErZffojgS7K/qsstffQgQ5LYEA8l
         kQU7Mcu0YHxei9bmeH9Szluxr2rDc6PnaWZcY8H1gLwTLE7Mpuv8WecTCrZofsSP8DWS
         K0iLKmFEeuAyFPIqaWBRI4Cv1rbXGh2nAdGAkYkPsHANNZq+DZrJbrXMOCdawHB1MIdW
         wSO1z6q0JzUt3D3ZrDjcbBgpiH0rI7oMfo7Yu2n9F3k+QziifHC22OsG5aFl8aGc0fYe
         v8Dg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=1CTEk/7jzE9VZCjfM4aS2iEqQEU9evMwKPg32Vd0tKY=;
        b=X/A7U57CZW3WvQjQYQuh6Ht9GpthX/TlAedgBlulPpvpfUDMVzq6pH5J4JA5oOS3VW
         hNiEBP0DQkOw9/8epOsGgLd87TDQAUyIKRX7Tjb4egXIA1sByjmDqQC2I1t/ySRy5s+l
         VVevQTwxaBCCC3duAhuOqcoAkosHi7ehuk5X9OuNDlo5S+Apl62sFC4mBnl2HLidwnwR
         4/9fR5syIQSyq7wTCJKMIZhjgwlYUx4dK68AEMmcC8tK6abbx+2BPmj6o4Tw11unh9sD
         wwUkYrMyNB4ocCQDZx8f66YPL1i/4BgC2jzLxB27RtC1aa3iKFUqnYzChJAdLM8hyWWw
         TRjw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=UGWTtStj;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=AKqESuP+;
       spf=pass (google.com: domain of 0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com
Return-Path: <0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id j5si5352030qtl.97.2020.12.18.09.03.32
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 18 Dec 2020 09:03:33 -0800 (PST)
Received-SPF: pass (google.com: domain of 0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=UGWTtStj;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=AKqESuP+;
       spf=pass (google.com: domain of 0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1608311012;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=jT1Gq8fp91mhGXpCcsoUaRl1kwtooSZaXgH1iNRZBQ0=;
	b=UGWTtStjfT7b+Uy3SrylguiRYDqYRSJXoKqfyMsCyUL3z9EMoRY1d4UBVhIWgjjE
	d60CvyUm9h7tjNyIn5pOzM1pwHhaHPEX4qKMlphU7lFdFWUJiAHZCkn5CdWcegA+9ki
	1IKV31zrXUDgNjigrQAcTX8bzs82clXg20+HTgBM=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1608311012;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=jT1Gq8fp91mhGXpCcsoUaRl1kwtooSZaXgH1iNRZBQ0=;
	b=AKqESuP+MsYCPgvjRcGdKLzO3puxrgtAZ4lW5W1zBYRrsO8BDLORKdap71HjJmRv
	bvqe74ATLVCRhNU7voqxD+E4SXWJUSYgQUhtE1OCtawszFo6DShqMV13YjgKJaI2sqE
	nrxYkYVgb9tSatKpcx4YKcLmokMC98iYnvEWb0as=
Content-Type: multipart/alternative;
 boundary="--_NmP-2a916e20ff64c7eb-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #298 [Easy] 
Message-ID: <0100017676ce7d12-7930f269-d166-4748-b102-6160f067d69d-000000@email.amazonses.com>
Date: Fri, 18 Dec 2020 17:03:32 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.12.18-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-2a916e20ff64c7eb-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A girl is walking along an apple orchard=
 with a bag in each hand. She likes to
pick apples from each tree as she =
goes along, but is meticulous about not
putting different kinds of apples =
in the same bag.

Given an input describing the types of apples she will =
pass on her path, in
order, determine the length of the longest portion of =
her path that consists of
just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion =
will
involve types 1 and 3, with a length of four.


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
----_NmP-2a916e20ff64c7eb-Part_1
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
    <title>Daily Coding Problem: Problem #298 [Easy]
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
Google.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">A girl is walking along an=
 apple orchard with a bag in each hand. She likes to pick apples from each =
tree as she goes along, but is meticulous about not putting different kinds=
 of apples in the same bag.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Given an =
input describing the types of apples she will pass on her path, in order, =
determine the length of the longest portion of her path that consists of =
just two types of apple trees.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, given the input <code style=3D"font-family: monospace; margin: 0 =
2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">[2, 1, 2, 3, 3, 1, 3, =
5]</code>, the longest portion will involve types <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">1</code> and <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">3</code>, with a =
length of four.</p>
<hr style=3D"font-family: Arial, 'Helvetica Neue', =
Helvetica, sans-serif; box-sizing: border-box;">
<p style=3D"margin-top: 0;=
 color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;"><a href=3D"https://www.dailycodingproblem.com/subscribe?=
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
----_NmP-2a916e20ff64c7eb-Part_1--
