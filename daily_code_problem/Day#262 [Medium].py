Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a05:6520:347:b029:96:b059:cd27 with SMTP id gm7csp529022lkb;
        Thu, 12 Nov 2020 09:03:12 -0800 (PST)
X-Google-Smtp-Source: ABdhPJxFgPd+9BsnIGsCqzaYCqA/q+tacVOuYUrUAjAH/lxMaZo8SebVU1M7s6scv/PYT0hpDsMc
X-Received: by 2002:ac8:7686:: with SMTP id g6mr74171qtr.125.1605200592461;
        Thu, 12 Nov 2020 09:03:12 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1605200592; cv=none;
        d=google.com; s=arc-20160816;
        b=e8iF/bTD1821ztkVusYdrHCEu/EsbjBiMFCT549eIRX7E+dyKkAKpPLYXGFVHVGzim
         9pX8+YrcGGHbM389zHhlAn3RFJ6cN7V8oXHfZizE84i7ZduH4sU52npWJluLFqaQc1Zo
         2Kxn5BsJr0eGkDoKtbxRZVz8LuLnoUBi4EVFFhjEQ8PqxQYXurUSZ2e8Nhy467/bBscr
         tgI8T5ZEvWa8HFUDU/0pIQTe6Ex5GRjPX5UjU2PXAmdT2plwbROQvMG/KMrjpmpyDzNf
         KmkxH4qU/Y12TuFIodPI7nbvH5LuOH6sIdiQWrCYsYu/V1oiFOiL7GGNr0mz7oKwpfIO
         kwIw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=9h7Tg2oLA7fFzOgnBP6hUGdxxdFX3epnG3Yhp9yvy/Q=;
        b=vHfvxAtZe/Aw8J+V0pRj0Qm3wqv9egz6p7kv4MtQGXIkEIfqXauHLQAg+XrI6vlky5
         DO/Ff47glCKuNZ7YEpqXBXnjXcBYBmVKe0YDUicppKNK0Du81nfCCeDeKIEch2h+pC+C
         V20j1ORb6LAHg3rIhq8GOd1m+KrfVCMbT5UnRM7b0xtj5FbpKVlvtZxy0a+bcr2rj0mV
         QSYx17QDYxOK9o4gXm4WfG6MTmvg9MBOEX/SVp1N4cm/UMbcfemFRXd7DWVd7laBT2mQ
         WBed3VWJTHhNYXaPZcvA8v5XdTZFYbGO415Nf/y/7yAOzsBGaonv1ez5pp83fnASEKW4
         s0kA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b="I/rXKAg8";
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LOKQDXvZ;
       spf=pass (google.com: domain of 01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com
Return-Path: <01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id x12si3137042qto.358.2020.11.12.09.03.12
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 12 Nov 2020 09:03:12 -0800 (PST)
Received-SPF: pass (google.com: domain of 01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b="I/rXKAg8";
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=LOKQDXvZ;
       spf=pass (google.com: domain of 01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1605200592;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=MABICTmoXpd97sYLh7Q1O4JsQ0na1bpOMjB0hJzh1yc=;
	b=I/rXKAg8klCEB4dWA/KJ74cQh86STr8wLr2UUCsnmI5eD1gXXIpk0eVgbAAVPa5Z
	zjlEPHZG8vFN1VsZ0Ds7VTY+ujD3QO6WtB1TrsEz/5P9JQw8BOHLs89Dvp9eUCY83RY
	d+UUEzNuUeOHdQBt+aRaFnXwNTG9fvsqWBdnZJEk=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1605200592;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=MABICTmoXpd97sYLh7Q1O4JsQ0na1bpOMjB0hJzh1yc=;
	b=LOKQDXvZBQEMH9hT46fpKAqpIRSTaPxxSRlKJ0TOaoruarvDaur74jourTepsBBj
	Fa8ZdBEROA7p4+X5wcvPWCk/aNZixUTN07UZFmV31Lj4MXETGgsVOdix0l0tKDrLd33
	ja33y/mHf0U1uukIynBAf12ljqTzWh9laVwwqXKQ=
Content-Type: multipart/alternative;
 boundary="--_NmP-6b8dece496b13570-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #262 [Medium] 
Message-ID: <01000175bd693b50-ac967bb9-05bd-485d-b53f-7a86c5d2c4f2-000000@email.amazonses.com>
Date: Thu, 12 Nov 2020 17:03:11 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.11.12-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-6b8dece496b13570-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Mozilla.

A bridge in a connected (undirected) =
graph is an edge that, if removed, causes
the graph to become disconnected.=
 Find all the bridges in a graph.


---------------------------------------=
-----------------------------------------

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
----_NmP-6b8dece496b13570-Part_1
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
    <title>Daily Coding Problem: Problem #262 [Medium]
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
Mozilla.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">A bridge in a connected =
(undirected) graph is an edge that, if removed, causes the graph to become =
disconnected. Find all the bridges in a graph.</p>
<hr =
style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
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
----_NmP-6b8dece496b13570-Part_1--
