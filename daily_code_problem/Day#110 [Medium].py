Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:86c1:0:0:0:0 with SMTP id j1csp552894ejy;
        Fri, 12 Jun 2020 08:42:48 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJw9UzGnxnuA7AQyTA+y36Z8WFHMco3iuBE+DaB0aIDsco9Mg00CJhri89pCb4zM4N7+509i
X-Received: by 2002:ae9:ebc5:: with SMTP id b188mr3605567qkg.203.1591976568366;
        Fri, 12 Jun 2020 08:42:48 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1591976568; cv=none;
        d=google.com; s=arc-20160816;
        b=eQ4e57zaPGgCq8g73w9pvHDsElJa7C9pZmP0Pof4OT1gjLi+il8UKkRpEGYlLNScPI
         jraNTLD5CIQt4NjrD0VbYOGbyDOjx/mCpGtc6IhOS93S/kiWmY/4v/samD2ahIX+Qs+7
         CA/Nawyf6bkUGtXUYpFU9+FKlzdj+X5OEa/0kbl5WQfiqghCyuYP/id4J5IdUA97ov52
         UjGgOYtZNIDnSZf2dtEiGIR6v97nJUQMdFbRdwk65uYD01fa4QnrUtRVxkA3re2IkEUT
         ds11nXHzUyFq/VFLZl7/Vf4Enu/eARCmxUWBdCNBkPNFT710gk5LurlapJSqALaaYhzC
         MBQg==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=v8qhZrZ/Dyjr1L2oYdkvCpkC33k/DP16drdg6b8yePE=;
        b=R4DLeaq33VGcR2ka+WWiqF5IJBwE28P4dqSma38gfbxVHavwu7WNlhn3ag+Ujeu7s8
         rAWIDu6S180TYxm1wDddpnm7vLX5ElQFJ6p+18tn/iMTTWli6+1eW5MteH2g03d5/nH/
         1VxwFvk896n0NhcTy9mNZ1o7/W402npNgBfpXoGc+7DMamSLXllLWuLVgqmdgU6P6dSh
         Mxxl09X3SeOeRF9ab4eBON/V20TfYXrxNqc/eIsKbrYqusIbSljcJldrOhIjt+Rqd54f
         A0IyIHwW8JFA8dCPlWeCj3u8pUtW4+QjM3BNPv7JA9C6dlq4SPHcafp0U5QrvX7LbmfW
         cVmw==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FEmm4BjE;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=ZcaEKVpj;
       spf=pass (google.com: domain of 01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com
Return-Path: <01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id i54si3706270qte.367.2020.06.12.08.42.47
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 12 Jun 2020 08:42:48 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=2efhd7xbwzuvvehkdwv6avycn2dw7g77 header.b=FEmm4BjE;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=ZcaEKVpj;
       spf=pass (google.com: domain of 01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=2efhd7xbwzuvvehkdwv6avycn2dw7g77; d=dailycodingproblem.com;
	t=1591976567;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=y2phy4yuJ9JB+GB/kC1upDHv09+ReZSnuaJ3+FDI7ws=;
	b=FEmm4BjEk8xe+rDXz80Vj7R96QHS5Lxz4gJuuA+nsnj+QkQ6xG3MOVmgh4n1gx3w
	PQEM+o+R9cbSCHePFB2037JKbdT01VNQb7scALKeaBgQ++anEt1GLT5iTbr2Ua5AwJE
	Yt+zjXMuw4rNgJwzsI7wVUggFCmzniHJonp25bco=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1591976567;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=y2phy4yuJ9JB+GB/kC1upDHv09+ReZSnuaJ3+FDI7ws=;
	b=ZcaEKVpjOVh3EdrL4veHmwRdglqwtu++HzO4Gz8UHHFJ2CpZ8oeegl6Fn9uALADy
	Y36S3QeAAWS6MWcvhgZ6We7ZgycbnGA26BxMPOf7etyE1Db9m5fCtt1QRk6fD9K+k2w
	9OTmbAa/gbpK89HzIPOfJ7pN+OYVIcZy77lEgBjU=
Content-Type: multipart/alternative;
 boundary="--_NmP-3f50299b511e8d81-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #110 [Medium] 
Message-ID: <01000172a932a157-daf54d17-25fb-4478-93ef-cc534347df1e-000000@email.amazonses.com>
Date: Fri, 12 Jun 2020 15:42:47 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.12-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-3f50299b511e8d81-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths =
from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5


Return [[1, 2], [1, 3, 4], [1, 3, 5]].


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
----_NmP-3f50299b511e8d81-Part_1
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
    <title>Daily Coding Problem: Problem #110 [Medium]
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
Facebook.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a binary tree, =
return all paths from the root to leaves.</p>
<p style=3D"margin-top: 0; =
color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">For example, given the tree:</p>
<pre style=3D"background-colo=
r: #f8f8f8; border: 1px solid #cccccc; font-size: 13px; line-height: 19px; =
overflow: auto; padding: 6px 10px; border-radius: 3px;"><code =
style=3D"border-radius: 3px; font-family: monospace; margin: 0; padding: 0;=
 white-space: pre; background: transparent; background-color: transparent; =
border: none;">   1
  / \
 2   3
    / \
   4   5
</code></pre><p =
style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.5em; =
text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">Return <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">[[1, 2], [1,=
 3, 4], [1, 3, 5]]</code>.</p>
<hr style=3D"font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">
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
----_NmP-3f50299b511e8d81-Part_1--
