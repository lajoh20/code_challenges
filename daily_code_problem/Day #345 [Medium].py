Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a9a:3ecc:0:b029:bc:7465:3c68 with SMTP id s12csp432483lkd;
        Wed, 3 Feb 2021 09:20:31 -0800 (PST)
X-Google-Smtp-Source: ABdhPJyQCWrNhpBxb3QAqICGshRiyKiIZPdgo8XFUF39LLSYeV/2/2ErJ1EqPFhlOOTIX3oWsoyd
X-Received: by 2002:a0c:b286:: with SMTP id r6mr3783214qve.40.1612372830840;
        Wed, 03 Feb 2021 09:20:30 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1612372830; cv=none;
        d=google.com; s=arc-20160816;
        b=uNRUGNKyVP/Z5x9e/DtvIM5JP60hxrX9uz20H7mFKPY50KFQk8km6Lg2+dwnC+lbO8
         j1a7tSVXl+Ut/rwEk7Y8K1lXVxKxdHzU4703Ry7K1JRZ553gvRJkTfW8drGHp5aNTV11
         qFMcqB5z4GHymk92zD9ISgKjAqZAArwDR7edUHkILPAnMuAmDewQb61rJYs0fAQAvKXb
         kPxl1Q9K5ISbKs2/PvMQEzLNiGmruPQcNG+BFJse8xihnJgpVPud2aOAYwH6lotaMLxR
         hlEtgkxdqYUaeBLl1PSn0O5SESWvGjeNp0oZCppO2VM9oTOWSbK2ElZ/pc2rfDcYqAWL
         /etA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=hNjJTJ5xJWm3vReKzsdZCKFyYjP0B4IXfsjC6jpP3rU=;
        b=hYdoAzEq7xSd+1fvivenJnrDwMHtOOBVOvKfMlyvFcfq3SOPDAAVIfbM4wgJcd5AEP
         fGGBmLgctR0qd8UEAxtuYIH2rSsSBXsZ9h2IocTdsPC75lxETjsbqnfpZbB2QAbPvZpw
         PR0yA1Tj9Gf0JdX59gMfnYhJaQer8GEXDXSxaX9eKkn25wGoigEj6BmplluTchyP0uy6
         YtE3RSVWliQI9AahesoHJEjq83F/4JWwbDKdOH8E94+thptwKFv7lV8/KkGeXjDuDNi9
         sfdOtwoABUcr84tUNi8zIgdUN9DA67nNpFSi/Dxvqq3mxo0Y7VisJHEw8IA/4TeoI2c1
         N9Mg==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=EkQWD6qY;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=bWUt4S8Z;
       spf=pass (google.com: domain of 0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com
Return-Path: <0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id b26si1278508qtc.40.2021.02.03.09.20.30
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Wed, 03 Feb 2021 09:20:30 -0800 (PST)
Received-SPF: pass (google.com: domain of 0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=EkQWD6qY;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=bWUt4S8Z;
       spf=pass (google.com: domain of 0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1612372830;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=u8RRheehrVm7WzRiH/Ty513D6dm4qdcIg7wTAJoS9aQ=;
	b=EkQWD6qYhGP2NimPxwDUqifNyk5l6Uz8PdpKvl9Fy3Wg41+UAowzs3iP4OgTWFDX
	0gSdfV8GPNo91EjxWR6Is/9b8UcK9dpoHpCANiosLYn3hR22C7kZml9eZKrIeiktc4g
	FMJRhST40h+5l1HhWzD9HfC6eV2D+b7bfkJN57oY=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1612372830;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=u8RRheehrVm7WzRiH/Ty513D6dm4qdcIg7wTAJoS9aQ=;
	b=bWUt4S8ZCqORCTCz/oHboysAblpxD3S9s7CFmj6iHsaSmycQgPS5gW4wBDm/IVVW
	tHS2dbFM+LlMhsvgStT/W4JSDr/qiI0gpBlyFnN2d614PItO+y0seleSd1CrA8eeus1
	gRpNGOIm2BUSqbh6Id1VcLUSphTsrCl0l43TD5qA=
Content-Type: multipart/alternative;
 boundary="--_NmP-a500c003d00e1d31-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #345 [Medium] 
Message-ID: <0100017768e8e852-292d38b4-00b8-4f38-adc4-50d9f1b4ff16-000000@email.amazonses.com>
Date: Wed, 3 Feb 2021 17:20:30 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2021.02.03-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-a500c003d00e1d31-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a set of synonyms, such as=
 (big, large) and (eat, consume). Using
this set, determine if two =
sentences with the same number of words are
equivalent.

For example, the following two sentences are equivalent:

 * "He wants to eat food."
 * "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c):
consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b=
, c)?


-------------------------------------------------------------------=
-------------

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
----_NmP-a500c003d00e1d31-Part_1
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
    <title>Daily Coding Problem: Problem #345 [Medium]
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
 Helvetica, sans-serif; box-sizing: border-box;">You are given a set of =
synonyms, such as <code style=3D"font-family: monospace; margin: 0 2px; =
padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">(big, large)</code> and =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">(eat, consume)</code>. Using this set, determine if =
two sentences with the same number of words are equivalent.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, the following two =
sentences are equivalent:</p>
<ul style=3D"text-align: left; color: #555; =
font-size: 16px; line-height: 1.5em; padding-left: 24px; font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;He wants to eat food.&quot;</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;He wants to consume food.&quot;</li>
</ul>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Note that the synonyms <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">(a, b)</code> and <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">(a, =
c)</code> do not necessarily imply <code style=3D"font-family: monospace; =
margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px solid =
#eaeaea; background-color: #f8f8f8; border-radius: 3px;">(b, c)</code>: =
consider the case of <code style=3D"font-family: monospace; margin: 0 2px; =
padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">(coach, bus)</code> and =
<code style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">(coach, teacher)</code>.</p>
<p style=3D"margin-top: =
0; color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Follow-up: what if we can assume that <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">(a, b)</code> and <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">(a, =
c)</code> do in fact imply <code style=3D"font-family: monospace; margin: 0=
 2px; padding: 0 5px; white-space: nowrap; border: 1px solid #eaeaea; =
background-color: #f8f8f8; border-radius: 3px;">(b, c)</code>?</p>
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
----_NmP-a500c003d00e1d31-Part_1--
