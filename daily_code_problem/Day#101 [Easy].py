Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:86c1:0:0:0:0 with SMTP id j1csp748005ejy;
        Wed, 3 Jun 2020 08:41:58 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJx4x3dgRk6HmEXs9ZFQjnKA7zJ5sTesT04RWTafO+As6VPkUd0ieWYMJh7Xr5NzVfZBDsu+
X-Received: by 2002:a37:b901:: with SMTP id j1mr177908qkf.427.1591198918277;
        Wed, 03 Jun 2020 08:41:58 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1591198918; cv=none;
        d=google.com; s=arc-20160816;
        b=Zl0bnigaiDRs5kDJpx1msRfN3pxnJvCwTaUo9zVpn75fVhLWTerDGF+zlX+le15ySS
         UW2x1x9AZ4sHZ8k7rXeh8TuTLcJSJXgpAWrpe6rJ8dHSusSDoL+1ApQQucdYzwsDdVli
         QZs2DsoBmCFryWPpbN40Vb02J+VbmQ9LVB1mq9OnbVro48QX5Uk9/te9ZydAu2OHmjNH
         YVP0GhbHVz0PQbjF5Elf9OaGMR5ADYFsYf/UPM26GV01c0sG7X6Bkb2AC7/SmDVqh9ux
         Eu/5rrRn3wrEP+jfrsGoM6grtPjNfMVH7R05peTflET9oYu2eO6+OsSQY01p7Gkryv4f
         O2IA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=CSNkqervnJuhY5hDvEsLFiLktmfJZIdrSDuTkzlUPR4=;
        b=Fxhw+mRTwNzckC0f572JnzaXdOODHBxr47oJF/iq8Z0bRK65aAXFXuyzK1JlBjU6Tc
         HQeLXyte5Mo2kgdaSAZoclaRHhOxbvEylPyDMcoGs7AgHChnTeY8BfWajWBOkNU03/Cx
         qBlFLde1pUfa7gM0G+GnhRZ48ek5aUqkLzikXkcfzkrfz3hUGcXsLEsJdxfqoT70QgNl
         0NgiUQWrZQ8/Duche4YBpD/olsn6FNr3bwWEoGgX1auO3VN4zekSRdOPKkO9YYyZo8Ep
         EaNTbdOWtlVlvT5F+xWDRww73AB8dUg/8Clza8Ivb/oAK1QLCEs8fR8OgX8+JKkENiy/
         +/CA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=LDwJ7mJw;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=IMW8jbtj;
       spf=pass (google.com: domain of 010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com
Return-Path: <010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id b66si1127383qkg.209.2020.06.03.08.41.58
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Wed, 03 Jun 2020 08:41:58 -0700 (PDT)
Received-SPF: pass (google.com: domain of 010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=LDwJ7mJw;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=IMW8jbtj;
       spf=pass (google.com: domain of 010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1591198917;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=lF0FqzD/j7xHYgAgGMY9OJHwlhnd46b96IBbe059BaM=;
	b=LDwJ7mJwA7wnVY+WQ9BBRl3sbURYhK+U4FN3GQKPCu1I+V5w34PmPkyHrrH1GcnI
	z578GP6TY8t5xsPfkVFUujMGwyHkPpXI4ASLcPGkWglSQpyrkHoBpp6JpEscZds8zbp
	S1KqKhPhXhyCo2R4F5ERnbV1JOBkWbGkAVeWXq3o=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1591198917;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=lF0FqzD/j7xHYgAgGMY9OJHwlhnd46b96IBbe059BaM=;
	b=IMW8jbtjNR+AJW4tbu9WOBruGi4tRimUUW+/CKAxfih2h146mvCx9Ww8s5FY9fpi
	7/WKn3mkc1y2kNA8dbOX/Gun/1lu53WnzlKaBZIrFp0ILn8sWWXPWh1duWWv1VUtfIc
	Yh1vUSfmXNlEHuKXsiURSqdIA2bC+UzIlFY4qtzo=
Content-Type: multipart/alternative;
 boundary="--_NmP-a66240a252d490d0-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #101 [Easy] 
Message-ID: <010001727ad8a4ed-126d035c-300c-4d5d-9c55-b7d16e835880-000000@email.amazonses.com>
Date: Wed, 3 Jun 2020 15:41:57 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.03-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-a66240a252d490d0-Part_1
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Alibaba.

Given an even number (greater than 2), =
return two prime numbers whose sum will
be equal to the given number.

A solution will always exist. See Goldbach=E2=80=99s conjecture
[https://en.wikipedia.org/wiki/Goldbach%27s_conjecture].

Example:

Input: 4
Output: 2 + 2 =3D 4


If there are more than one solution possible=
, return the lexicographically
smaller solution.

If [a, b] is one solution=
 with a <=3D b, and [c, d] is another solution with c <=3D
d, then

[a, b] < [c, d]


If a < c OR a=3D=3Dc AND b < d.


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
----_NmP-a66240a252d490d0-Part_1
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
    <title>Daily Coding Problem: Problem #101 [Easy]
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
Alibaba.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given an even number =
(greater than 2), return two prime numbers whose sum will be equal to the =
given number.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">A solution will always =
exist. See <a href=3D"https://en.wikipedia.org/wiki/Goldbach%27s_conjecture=
" style=3D"color: #3869D4; font-family: Arial, 'Helvetica Neue', Helvetica,=
 sans-serif; box-sizing: border-box;">Goldbach=E2=80=99s conjecture</a>.=
</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: =
1.5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Example:</p>
<pre =
style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; font-size: =
13px; line-height: 19px; overflow: auto; padding: 6px 10px; border-radius: =
3px;"><code style=3D"border-radius: 3px; font-family: monospace; margin: 0;=
 padding: 0; white-space: pre; background: transparent; background-color: =
transparent; border: none;">Input: 4
Output: 2 + 2 =3D 4
</code></pre><p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">If there are more than one=
 solution possible, return the lexicographically smaller solution.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">If [a, b] is one solution with a =
&lt;=3D b, and [c, d] is another solution with c &lt;=3D d, then</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">[a, b] &lt; [c, =
d]
</code></pre><p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">If a &lt; c OR a=3D=3Dc =
AND b &lt; d.</p>
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
----_NmP-a66240a252d490d0-Part_1--
