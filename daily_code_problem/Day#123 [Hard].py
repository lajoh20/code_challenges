Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:1385:0:0:0:0 with SMTP id f5csp1686271ejc;
        Thu, 25 Jun 2020 08:47:32 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJz5Uri6+viFVvUN5wTrl7+FrDz8InWilRoVfKPtr8iyVWGteVULcM0pgZPivNEkihH6TrEX
X-Received: by 2002:a0c:aed6:: with SMTP id n22mr37013371qvd.70.1593100052584;
        Thu, 25 Jun 2020 08:47:32 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1593100052; cv=none;
        d=google.com; s=arc-20160816;
        b=sazVX5mVMBNITmg0U11lC2E5rSW8cRCgd6OtKM8KLbFh2ftdVzCxWgVsW1UOaakED5
         QCYZBIiDp5oK2tDapezE9l7MKPGjTtbKsnVqSJfcOLAsSN0ohAVzRmei09ZzCTdb5LOU
         vneSgasAY46makhOt4kkqyudVeOJgLne4qZBvtUHO686m2aBDr0qT/BgzOdLaYOGWTsZ
         MoUP8VrPIb2WSeyspBgxTGM47NcRa3H2zVCIo6yp3QtUQDPSmDtdoOt+MBZ+AqXbnJ9V
         LtrVz+cf0oibUJtP7IX+SgPw/HdrU3Yz7aNShnmYRqrbK/VfT4hNjHDbXDnnjj1DR7p2
         oAYw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=abvON50jzRE0ZLr4HhGqF2isWSvISBY1kD78wyZuvqM=;
        b=UeDpq44A/ol/rY/u78cF6OQc4eBM/znsIzRlgxvE1CQWZTCgW04I68pBOKPr+veSqa
         Yc6ZOT8ffbUQagOzJQQ7ZluXHCcnpahzY1xeUZB4+AtY9Dof2QHYpMV+fUylqLmHd4VR
         nwHJ/1nFU2+clz84MFlRrREV2vo+C8u0jfU8io+zxPoFI3+C9dpgYBJZlrmR1Pc5MZK9
         /WP0QQjnDliamGr6jdRUL05FLsv5GbvFI6YHYTEOARaebnN7o7hpUA1+cRXkqyr6DNJ5
         b1CiDd9SDRqs6Lc4aIHLP4Blf+5rPPURYPC10JB92qy36zAXeYPS5x5/lgan0KDVfU3p
         +HMA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=iD580Eut;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=GEb2PsXr;
       spf=pass (google.com: domain of 01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com
Return-Path: <01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id n23si10429203qkh.168.2020.06.25.08.47.32
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 25 Jun 2020 08:47:32 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=iD580Eut;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=GEb2PsXr;
       spf=pass (google.com: domain of 01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1593100052;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=MX+Zuek1BFCoD9LkaOWSrRCg16f1/Q1fdgLMSapr09U=;
	b=iD580Eut00BNTUQvAZj7zw2yRMrZCq9o7fWsy9XfgZOZVo/FPISn64ugArt32Vey
	kkvTHVr0zzTJSGxkRMCrLo6DnMSyppSxpGBCL263poMg+RkOXyWI3/Ny2LMv7oxSwYN
	49UlvfSsRWHK1OdBRXFcdvLkgc+XcRmek+hGRExs=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1593100052;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=MX+Zuek1BFCoD9LkaOWSrRCg16f1/Q1fdgLMSapr09U=;
	b=GEb2PsXr0+atyyyNo7mTHx++Z/XYvJUZp4KhgWxIWF4othRsEWSh1xdNa9TiFJvw
	VFbMV91Lo1UNuOyCKvgc1KttFMS91W7FIES4QC3SNskN/bUQ3IXXvz2TjpRqqGdu6EJ
	DlnWqVIBWc9mn5JSfPZrAvyaHj0SGbmYGI72Wsuc=
Content-Type: multipart/alternative;
 boundary="--_NmP-4c92486c6a6b6803-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #123 [Hard] 
Message-ID: <01000172ec29a69e-6fcdc959-8cad-4da7-b257-d9f9510b8567-000000@email.amazonses.com>
Date: Thu, 25 Jun 2020 15:47:32 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.06.25-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-4c92486c6a6b6803-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a string, return whether it =
represents a number. Here are the different
kinds of numbers:

 * "10", a positive integer
 * "-10", a negative integer
 * "10.1", a positive real number
 * "-10.1", a negative real number
 * "1e5", a number in scientific notation

And here are examples of =
non-numbers:

 * "a"
 * "x 1"
 * "a -2"
 * "-"


--------------------------=
------------------------------------------------------

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
----_NmP-4c92486c6a6b6803-Part_1
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
    <title>Daily Coding Problem: Problem #123 [Hard]
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
LinkedIn.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a string, return =
whether it represents a number. Here are the different kinds of =
numbers:</p>
<ul style=3D"text-align: left; color: #555; font-size: 16px; =
line-height: 1.5em; padding-left: 24px; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;10&quot;, a positive integer</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;-10&quot;, a negative integer</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;10.1&quot;, a positive real number</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;-10.1&quot;, a negative real number</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;1e5&quot;, a number in scientific =
notation</li>
</ul>
<p style=3D"margin-top: 0; color: #555; font-size: =
16px; line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica =
Neue', Helvetica, sans-serif; box-sizing: border-box;">And here are =
examples of non-numbers:</p>
<ul style=3D"text-align: left; color: #555; =
font-size: 16px; line-height: 1.5em; padding-left: 24px; font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;a&quot;</li>
<li style=3D"font-family: Arial=
, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">&quot;x=
 1&quot;</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica,=
 sans-serif; box-sizing: border-box;">&quot;a -2&quot;</li>
<li style=3D"font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; =
box-sizing: border-box;">&quot;-&quot;</li>
</ul>
<hr style=3D"font-family:=
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
----_NmP-4c92486c6a6b6803-Part_1--
