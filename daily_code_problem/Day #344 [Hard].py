Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a9a:3ecc:0:b029:bc:7465:3c68 with SMTP id s12csp495825lkd;
        Tue, 2 Feb 2021 09:21:02 -0800 (PST)
X-Google-Smtp-Source: ABdhPJxGCrpA43rtYmLR8bbv5T7SdIRFXGnN7JGEyTRd19ehQqfZb4QRvFpDn+8jnZAoiaf8f3p8
X-Received: by 2002:ac8:4f52:: with SMTP id i18mr20102398qtw.113.1612286462242;
        Tue, 02 Feb 2021 09:21:02 -0800 (PST)
ARC-Seal: i=1; a=rsa-sha256; t=1612286462; cv=none;
        d=google.com; s=arc-20160816;
        b=p96e63kLZxfttkLhXmVH2AhcLPHHQD0Cvjq+ELJUrAI5aXhhU2I3VUOlOmDE2H5zXv
         r2pwXUoQPsiAz/OeEIeqZra8Gvb4y09xHk0LrdmaxtkM1EPqWoNiBaMAvmwtQg/kZV9R
         iFxsw6kWQB9x9/FUuWqKeL50oKtYiPsvHsVIZOwjy1RK3rVANONjkMeMQ0fKZVBIhDGp
         +P+2ktwNqy+2fEKByoQ+YkQJjEMRPLR4h4dUu+qNHYjQGYkqzR/+GTGWeNo2BwFXiBq3
         9SRKr2SJiaLauZUp6++/8cjGEu4ccsMu81VPH7CIuQ+q4uYe7qXoEq/AUPhkswiVdvJc
         eEfg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=MvdYbHRfVnlYSFlMloPoJ+yWah6lge9GnSx1kVS0ikU=;
        b=TdGR6djJJit1RzEH63Mr6C1WDRCc+S5RII6Ck+SR3RhHcpu63ylmKT8EfHE85VhLkG
         KpSUg8lImAS+lfZx3d7PJHha1Kmh1kmlMW/31CuJSMp7PkhjeGpbEo9kIon5N4CP40aq
         dDg+E7SVa1MTbUT0TmdNQsRg25yed0ynI7yxeltU+c0m/+2a9NDvpsA6GX/H4TSRZEP+
         ZMseE61QJgcTrzYeso5i3zjicFQjnvSd7fzEYi2Bk3EeS/b6tyU06UwXM8hBP5gq64k6
         66k/94C/0rUYsun4NVHAwAMcJIhHP0btxT663160T0brmUezBm7h9Fhpi6CJuWt/A/9A
         qjBw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=hW51CRof;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=PpJbzL52;
       spf=pass (google.com: domain of 0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com
Return-Path: <0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id u64si10851052qkb.23.2021.02.02.09.21.01
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Tue, 02 Feb 2021 09:21:02 -0800 (PST)
Received-SPF: pass (google.com: domain of 0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=hW51CRof;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=PpJbzL52;
       spf=pass (google.com: domain of 0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1612286461;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=8Sp+1irzIh+TcfamFLnNi6uB72b1jvd+zsoTlsxOoYU=;
	b=hW51CRof+W2kpOnpY49xhg1LpnxbLddh90Q4RTCIUrRzhnU7suuBS6b8GYS5UPT1
	Ihq0n3IjN1f3l7QTclgfIntSQZaadgrqqEfa1bjbAyaK9i9VH5Kh8fOmAlkZqXMtRmQ
	SmNo278oz7xH87g9FNiKW27vOHO1T3bqWxs60OQw=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1612286461;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=8Sp+1irzIh+TcfamFLnNi6uB72b1jvd+zsoTlsxOoYU=;
	b=PpJbzL5238ghQM2WeJHAlJokLj95r8CuuOOalWrH1JjnOKtLDNYMPX78f+xjWYo1
	Ew3RN+HYIfcrB1/1rqrOlRvla4RG83tols20+gHkxcpEQooNDd3J6bO+ZQ8jpI9ML92
	Sxo2kao9zk+3Vtz8qf+uud7CM3UvZHfM2UrMrRXc=
Content-Type: multipart/alternative;
 boundary="--_NmP-a551a838074d0f96-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #344 [Hard] 
Message-ID: <0100017763c306b4-a6864efb-cb36-4477-93be-411fd6d40251-000000@email.amazonses.com>
Date: Tue, 2 Feb 2021 17:21:01 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2021.02.02-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-a551a838074d0f96-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Adobe.

You are given a tree with an even number =
of nodes. Consider each connection
between a parent and child node to be an=
 "edge". You would like to remove some
of these edges, such that the =
disconnected subtrees that remain each have an
even number of nodes.

For example, suppose your input was the following tree:

   1
  / \=20
 2   3
    / \=20
   4   5
 / | \
6  7  8


In this case, removing the edge=
 (3, 4) satisfies our requirement.

Write a function that returns the =
maximum number of edges you can remove while
still satisfying this =
requirement.


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
----_NmP-a551a838074d0f96-Part_1
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
    <title>Daily Coding Problem: Problem #344 [Hard]
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
Adobe.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">You are given a tree with =
an even number of nodes. Consider each connection between a parent and =
child node to be an &quot;edge&quot;. You would like to remove some of =
these edges, such that the disconnected subtrees that remain each have an =
even number of nodes.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">For =
example, suppose your input was the following tree:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">   1
  / \=20
 2   3
    / \=20
   4   5
 / | \
6  7  8
</code></pre><p =
style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.5em; =
text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">In this case, removing the edge (3, 4)=
 satisfies our requirement.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">Write a =
function that returns the <em style=3D"font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box;">maximum</em> number of =
edges you can remove while still satisfying this requirement.</p>
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
----_NmP-a551a838074d0f96-Part_1--
