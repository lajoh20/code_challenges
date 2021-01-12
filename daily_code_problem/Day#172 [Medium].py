Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:3618:0:0:0:0 with SMTP id q24csp602699ejb;
        Thu, 13 Aug 2020 08:57:29 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyTFnY88khtVYf8je09Wzt0v4uLZCj8/L76ng/17uR48pPwUaPYJIgE63pWNRo/TQ51IjQ2
X-Received: by 2002:ad4:510c:: with SMTP id g12mr5267943qvp.106.1597334249728;
        Thu, 13 Aug 2020 08:57:29 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1597334249; cv=none;
        d=google.com; s=arc-20160816;
        b=T2KFZXYbq951vCPS/zNf/NUYoLXU7ASq6au61qnwInDrNEUWQ8tLj0FWxU54CTpJ2T
         pDPxrgEwD9IIFZvPdHMIkBTKTyV4P3yjJrXxq5zjy950CaH5TZOhIuTR5hEzGgK+MrUk
         GTMVspWUNGcNWMDrb113mVDdWn+DsKz4YMOfpoUBluiiyU7G4TW2LgUv2kaQDXoUAz0c
         U72UI0rJ7r4DQjYQ3VuOujDbXHbZSlrUpmvK1x/y0uKmt/mphwhSBFSFP90mYwcEVEPv
         +zmhon6c5S9qLg4zjtI3UKYyNGJQLBGg8sMze6QvkyTmnk1bO3H/nznnysbYdMqXBXFg
         AmPQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=5Cu2y+Wfwd+IvCWE/NYnDEd7kfQ5A2R82vIrJ/YwzBE=;
        b=fHN7U3a3dEA4E3k0s8xoyUzTtOj4eQzV0WAtINKuNGRW4buxZnlK8qJUcySEJoqGNq
         nEkV7zHdtXbmTplzsGQOQb+6hFXc6x2q6MrwSpNDRyJSMjV8izwE0rmm2Wz2J4KFvFwG
         /ugwsyuO/1WUzF0cKH7GSqa9eoho2zOgEQJ2bAkxTuCHD+rTGN9r6FUSSma0VZwQ6atV
         +LZsNOClTs1MhFAXFH81WYX7LeWxab+R/f8ANuRAmM9mB0YKozEOc/PbZeH6GyY8r4QL
         NX5W8Mhkk4uPOSm7afg7r4TMWqZFj3CSH+z+4yE0hUXkxeng8p0Vx2ieJEt1vJYVtZNv
         +IUA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=WyN+JN2h;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=fjpCrNbF;
       spf=pass (google.com: domain of 01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com
Return-Path: <01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com>
Received: from a35-129.smtp-out.amazonses.com (a35-129.smtp-out.amazonses.com. [54.240.35.129])
        by mx.google.com with ESMTPS id k26si3400709qtm.334.2020.08.13.08.57.29
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Thu, 13 Aug 2020 08:57:29 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com designates 54.240.35.129 as permitted sender) client-ip=54.240.35.129;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=WyN+JN2h;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=fjpCrNbF;
       spf=pass (google.com: domain of 01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com designates 54.240.35.129 as permitted sender) smtp.mailfrom=01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1597334249;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=nuDhTkMKpXD5CE0aZoSsCRzXtiZlg3erwMe1BengJBI=;
	b=WyN+JN2hARiLD1YZOilGWRkhy/+qurVd0J/x9SfUfa+Cpqg3OMFzTAzJXmBLtHS7
	1e8FF7pWnkhr0oZZk0ytm7Q+fZOvrv5FaIglGZ8L18WFqvTl2HTpx8Hbjq8Ex4qUzW9
	ilDsxZWycMxDVzLHzfCqQExGVUxbKM1ZlRv2VoY8=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1597334249;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=nuDhTkMKpXD5CE0aZoSsCRzXtiZlg3erwMe1BengJBI=;
	b=fjpCrNbF84WUYBVEsgGzSjHiQZOF+th83pynuU9XdnIcJexUqibLQEzoq8eun7B6
	VLzCoz1PIUOvoqQV0Vt7XFj7a2Q9yS7amvkUQHF2D0PSuJB+XZtsNpRkh3wj4uQWdtG
	JnPHzXXDemh7IwlMUOMGnsn/6Qmdg1d44RmI0N5g=
Content-Type: multipart/alternative;
 boundary="--_NmP-aa277cbb07dbcecf-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #172 [Medium] 
Message-ID: <01000173e88a5f69-eded2589-b4a7-4e23-86aa-700d4d0d2e83-000000@email.amazonses.com>
Date: Thu, 13 Aug 2020 15:57:29 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.08.13-54.240.35.129
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-aa277cbb07dbcecf-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given a string s and a list of words =
words, where each word is the same length,
find all starting indices of =
substrings in sthat is a concatenation of every
word in words exactly once.

For example, given s =3D "dogcatcatcodecatdog" and words =3D ["cat", =
"dog"], return
[0, 13], since "dogcat" starts at index 0 and "catdog" =
starts at index 13.

Given s =3D "barfoobazbitbyte" and words =3D ["dog", =
"cat"], return [] since there
are no substrings composed of "dog" and "cat"=
 in s.

The order of the indices does not matter.


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
----_NmP-aa277cbb07dbcecf-Part_1
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
    <title>Daily Coding Problem: Problem #172 [Medium]
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
Dropbox.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Given a string <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">s</code> and a list of words <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">words</code>, where each word is the same length, find=
 all starting indices of substrings in <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">s</code>
that is a concatenation of every word in <code style=3D"font-family: =
monospace; margin: 0 2px; padding: 0 5px; white-space: nowrap; border: 1px =
solid #eaeaea; background-color: #f8f8f8; border-radius: 3px;">words</code>=
 exactly once.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px;=
 line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue'=
, Helvetica, sans-serif; box-sizing: border-box;">For example, given s =3D =
&quot;dogcatcatcodecatdog&quot; and words =3D [&quot;cat&quot;, =
&quot;dog&quot;], return [0, 13], since &quot;dogcat&quot; starts at index =
0 and &quot;catdog&quot; starts at index 13.</p>
<p style=3D"margin-top: 0;=
 color: #555; font-size: 16px; line-height: 1.5em; text-align: left; =
font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif; box-sizing: =
border-box;">Given s =3D &quot;barfoobazbitbyte&quot; and words =3D =
[&quot;dog&quot;, &quot;cat&quot;], return [] since there are no substrings=
 composed of &quot;dog&quot; and &quot;cat&quot; in <code =
style=3D"font-family: monospace; margin: 0 2px; padding: 0 5px; =
white-space: nowrap; border: 1px solid #eaeaea; background-color: #f8f8f8; =
border-radius: 3px;">s</code>.</p>
<p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">The order=
 of the indices does not matter.</p>
<hr style=3D"font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">
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
----_NmP-aa277cbb07dbcecf-Part_1--
