Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:3618:0:0:0:0 with SMTP id q24csp861847ejb;
        Sun, 16 Aug 2020 08:51:40 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyaMbZJa8xqvN1CiUBic2Xla9Z5VekMOTrDy0O4dV95i6OxnJ1J5YunDN0G6qft0bYb1aTv
X-Received: by 2002:a0c:ea8e:: with SMTP id d14mr10637160qvp.37.1597593100589;
        Sun, 16 Aug 2020 08:51:40 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1597593100; cv=none;
        d=google.com; s=arc-20160816;
        b=eolz81MUVt+6bYqLnbBbrROuW0r0zf67c63hSmlICg4+V8XihCpqddiedRpeU20lRn
         5X98UZBEjafItxe1K84n4zZ/lnL05lQr/mdAqEo6vizphcwZeDuUmwa4Wl0+C7ZzCBTz
         eXysAGlJAmrUhR4Xo9J8opFA0hNWPBE58Spna5SHSorsS9+2Dnfo2HA8DDEwfKKe4PgT
         UQEtKMxR78rAmV88L4uSG2KSaWZCh6JxTpOVQ4VoUw00ymcva9a60cAccGdJpsrHtxvh
         INyVVhXyjcTw4T7X79Ep2oFYCL5bJIuTTQYp37S3UduO7c68Q15vqXdeoQ1xebz6VgH7
         015g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=sDqag5LH8zo+qse9KcNq6aWT1Sv58mU/T0rSdAG1PsU=;
        b=AInl6v2shSnI8Q1XMAmv84s9W1OVDE04gSg4Z4PoaCkkiHdFk8mklgpRxR9nBZMain
         iF6bNJXHJJW7mrqPwLOUW4Ihn81TyUXTayn0lcLFLZRaYOeEBU372kBfP7Uv81BDMH2r
         AX0FfLxwxy9QGLNXL/ApNEU+JEz8OR1jc4C8v5eQbuM+ht9cEKNS5GkrC2InTF0aAN21
         D3XW3KC5S5zq+e33fdRPvxkoFksyQCDX7Ggf3J07qxA6XRPnsTxwD1VF98UDJVXDZtf+
         vg0Wz//xlZ1InwCRUmq9Crg7pBxiZIoQx29F4RYEWOYuPbjKCStlD0vLb8gReV2adBNX
         o3UQ==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=HAL0P7id;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=JLoH+8bI;
       spf=pass (google.com: domain of 01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com
Return-Path: <01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id v6si7070377qvk.96.2020.08.16.08.51.40
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Sun, 16 Aug 2020 08:51:40 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=HAL0P7id;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=JLoH+8bI;
       spf=pass (google.com: domain of 01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1597593099;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=XCKsmCE88XzkUqH0HfltR46GQHPg6aB16qrcfNf3c1g=;
	b=HAL0P7idZ7V2Y38K/Fz5U9M+osIRfNL/0LjpsJBpE2WyaXA5hPRAEJUqdFxOoxbM
	VMwZfMkT9kWi5hPoeSFe+eZVFczyn38R1AVqhgMyinytUfyxtRma7AulClFToxT5Ct7
	AkzQpp5JNuaQiJGpcrU2d/KnaVkLCmyNWljGo+so=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1597593099;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=XCKsmCE88XzkUqH0HfltR46GQHPg6aB16qrcfNf3c1g=;
	b=JLoH+8bISHcxlS+0tTy9K3K/5/Mu5Klgd4/Dv/yoqRUCGJWxWmsGWk9bK5KrDKLf
	H005cg3jH55RwnCjUxXxrHTOu/kUx36fe1vIKuL3mlD2+RSmaCB16ng98m/Bi4lhf1u
	UjkW6LeoRyQQkElkNC+ahfll3zVZ1FmsbSfQLFAU=
Content-Type: multipart/alternative;
 boundary="--_NmP-dad04c6406738c7c-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #175 [Easy] 
Message-ID: <01000173f7f81e11-92bb7ca4-b28b-42d8-baa9-2775f09e2121-000000@email.amazonses.com>
Date: Sun, 16 Aug 2020 15:51:39 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.08.16-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-dad04c6406738c7c-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a starting state start, a =
list of transition probabilities for a
Markov chain, and a number of steps =
num_steps. Run the Markov chain starting
from start for num_steps and =
compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the =
following
transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]


One instance of running this =
Markov chain might produce { 'a': 3012, 'b': 1656,
'c': 332 }.


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
----_NmP-dad04c6406738c7c-Part_1
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
    <title>Daily Coding Problem: Problem #175 [Easy]
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
 Helvetica, sans-serif; box-sizing: border-box;">You are given a starting =
state <code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px;=
 white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8;=
 border-radius: 3px;">start</code>, a list of transition probabilities for =
a Markov chain, and a number of steps <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: =
3px;">num_steps</code>.
Run the Markov chain starting from <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">start</code> for <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: =
3px;">num_steps</code> and compute the number of times we visited each =
state.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">For example, given the =
starting state <code style=3D"font-family: monospace; margin: 0 2px; =
padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">a</code>, number of steps =
5000, and the following transition probabilities:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">[
  (&#39;a&#39;, &#39;a&#39;, 0.9),
  (&#39;a&#39;, &#39;b&#39;, 0.075),
  (&#39;a&#39;, &#39;c&#39;, 0.025),
  (&#39;b&#39;, &#39;a&#39;, 0.15),
  (&#39;b&#39;, &#39;b&#39;, 0.8),
  (&#39;b&#39;, &#39;c&#39;, 0.05),
  (&#39;c&#39;, &#39;a&#39;, 0.25),
  (&#39;c&#39;, &#39;b&#39;, 0.25),
  (&#39;c&#39;, &#39;c&#39;, 0.5)
]
</code></pre><p style=3D"margin-top: 0;=
 color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">One instance of running this Markov chain might produce <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">{ &#39;a&#39;: 3012, &#39;b&#39;: 1656, &#39;c&#39;: =
332 }</code>.</p>
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
----_NmP-dad04c6406738c7c-Part_1--
