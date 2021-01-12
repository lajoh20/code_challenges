Delivered-To: lewisjohnson1066334@gmail.com
Received: by 2002:a17:906:3618:0:0:0:0 with SMTP id q24csp218588ejb;
        Fri, 14 Aug 2020 08:53:57 -0700 (PDT)
X-Google-Smtp-Source: ABdhPJyw3xF+kqp2KIH9HQZToUjt2ThAvJ2F6GQTKgD6oAPkaP/uh0I8K+KOSdv+5Ywsycd0onhr
X-Received: by 2002:a37:27d8:: with SMTP id n207mr2643514qkn.446.1597420436857;
        Fri, 14 Aug 2020 08:53:56 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1597420436; cv=none;
        d=google.com; s=arc-20160816;
        b=iFTORgAmP0XSXcsZlVMknAfpInmVXo2tZpZz7sqyoPtjpgiWXZ1IKBKU96X/qVw1kL
         ruOvoL5LGHAhIG19b2VQ7+UsSg4SW2US2nW4esnIido886aGut+4e0VEnfCdsPQQS3jE
         XbTO+OLheYCWj4O7m9CNif8gnIdz07F+q3ufMhoYryAq+IqioeH3neWs71VpaoFLYGeO
         3HxleVppBffgN2nlRxtCX9r0WbKyOWM3dz7ofzIMEc/CO2+SBfj4i6MnJazMKccYxdsb
         RZoaE+pU/H0KPFG2tLtgAkbxOdfzuyNRPGA5P/oNwJJvgXpd99zhSw38870b8RjwPKdM
         Cntw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:mime-version:date:message-id:subject:to:from
         :dkim-signature:dkim-signature;
        bh=Lcsv5PR867EKd4TqsrRYywwfj8JTcqHDpWDD7tE7zAw=;
        b=X0Qvtzjqj6rg+neljNMC9Sswj8MmX9qaZ/Hvx0AEDs+Nyd09VpKuI/PkEGAe/+Qgy9
         j2uiYVUaOXIJq9jcgsaCmwDlZBTOmv1jHquUumHLzpSvEOIDf7aain2hWM4qcGmzxIH7
         ysrQPj5rN4TCmry8ZZgkoLBgkdseky+/GCzIVghHyIApHei/sMAHU+pY9X3TAeSpKOKW
         BhounPXHm7Rz8+MXgu89YvP4H3+UOMW7AEpm7as0zSpw9f8ezGnX3vuxkp65QKo6qAlX
         o7563bSvsJpXzDJUt/c76NRJ3litg+BOmc/DFbjDcTqLLhnXg888XsAKjaHBLuYKfgV0
         mFGg==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=GxpPDMDz;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=eFOhdB0N;
       spf=pass (google.com: domain of 01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com
Return-Path: <01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com>
Received: from a37-140.smtp-out.amazonses.com (a37-140.smtp-out.amazonses.com. [54.240.37.140])
        by mx.google.com with ESMTPS id f10si524669qko.54.2020.08.14.08.53.56
        for <lewisjohnson1066334@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-SHA bits=128/128);
        Fri, 14 Aug 2020 08:53:56 -0700 (PDT)
Received-SPF: pass (google.com: domain of 01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com designates 54.240.37.140 as permitted sender) client-ip=54.240.37.140;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@dailycodingproblem.com header.s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5 header.b=GxpPDMDz;
       dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv7c2xz3womw6peuasteono header.b=eFOhdB0N;
       spf=pass (google.com: domain of 01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com designates 54.240.37.140 as permitted sender) smtp.mailfrom=01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@amazonses.com
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=fs65dhbqnjtxpwh3w2hfcyjff7s3hra5; d=dailycodingproblem.com;
	t=1597420436;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version;
	bh=EARKcM8yTDXFFdvv1NwHD73DqqACxp6ZYPmf1L1WFVI=;
	b=GxpPDMDzkr7Q/GyfIsH3ULxZ104tv91ja/aNlPhyVCTWfElzU5+bhuj/3m2PC4TL
	qFdoTyLtj5ZcbTBt+F1P0f2TuQxj9vCJQuHLQEUuNSK4OABuEjWUNckmva3EKxXs1nF
	d65RdKypTaRlO3et8EnMT6gPpXBLAGOf9L0lXA7E=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=224i4yxa5dv7c2xz3womw6peuasteono; d=amazonses.com; t=1597420436;
	h=Content-Type:From:To:Subject:Message-ID:Date:MIME-Version:Feedback-ID;
	bh=EARKcM8yTDXFFdvv1NwHD73DqqACxp6ZYPmf1L1WFVI=;
	b=eFOhdB0NV/toyfcqhCqkNjb/h4bitQnHqgHj3kMJWMzBo4s1sXX6ILszOgOF4zN1
	tIMjsTJVAqjY3vT67dFnd8icOkQaX25d49Prw2NqjpDUA1LwtQNIG51mFq6CYB1FmNj
	3rE++Uxy4ZaxGzpqISt73X7NNPxedO6N58+KYtlg=
Content-Type: multipart/alternative;
 boundary="--_NmP-4a3807adb34bd6b8-Part_1"
From: Daily Coding Problem <founders@dailycodingproblem.com>
To: lewisjohnson1066334@gmail.com
Subject: Daily Coding Problem: Problem #173 [Easy] 
Message-ID: <01000173edad79e1-03ada850-d829-4218-a1e9-57e869531c07-000000@email.amazonses.com>
Date: Fri, 14 Aug 2020 15:53:55 +0000
MIME-Version: 1.0
X-SES-Outgoing: 2020.08.14-54.240.37.140
Feedback-ID: 1.us-east-1.wck0CVOMXpk3J1hWQUuT3xWrPkd7vNxfHtoFAXxS0WA=:AmazonSES

----_NmP-4a3807adb34bd6b8-Part_1
Content-Type: text/plain
Content-Transfer-Encoding: quoted-printable

Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Write a function to flatten a nested =
dictionary. Namespace the keys with a
period.

For example, given the =
following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}


it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}


You can assume keys do not contain dots in them, i.e. no clobbering will =
occur.


------------------------------------------------------------------=
--------------

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
----_NmP-4a3807adb34bd6b8-Part_1
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
    <title>Daily Coding Problem: Problem #173 [Easy]
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
Stripe.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">Write a function to =
flatten a nested dictionary. Namespace the keys with a period.</p>
<p style=3D"margin-top: 0; color: #555; font-size: 16px; line-height: 1.=
5em; text-align: left; font-family: Arial, 'Helvetica Neue', Helvetica, =
sans-serif; box-sizing: border-box;">For example, given the following =
dictionary:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid =
#cccccc; font-size: 13px; line-height: 19px; overflow: auto; padding: 6px =
10px; border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">{
    &quot;key&quot;: 3,
    &quot;foo&quot;: {
        &quot;a&quot;: 5,
        &quot;bar&quot;: {
            &quot;baz&quot;: 8
        }
    }
}
</code></pre><p style=3D"margin-top: 0; color: #555; font-size: 16px; =
line-height: 1.5em; text-align: left; font-family: Arial, 'Helvetica Neue',=
 Helvetica, sans-serif; box-sizing: border-box;">it should become:</p>
<pre style=3D"background-color: #f8f8f8; border: 1px solid #cccccc; =
font-size: 13px; line-height: 19px; overflow: auto; padding: 6px 10px; =
border-radius: 3px;"><code style=3D"border-radius: 3px; font-family: =
monospace; margin: 0; padding: 0; white-space: pre; background: =
transparent; background-color: transparent; border: none;">{
    &quot;key&quot;: 3,
    &quot;foo.a&quot;: 5,
    &quot;foo.bar.=
baz&quot;: 8
}
</code></pre><p style=3D"margin-top: 0; color: #555; =
font-size: 16px; line-height: 1.5em; text-align: left; font-family: Arial, =
'Helvetica Neue', Helvetica, sans-serif; box-sizing: border-box;">You can =
assume keys do not contain dots in them, i.e. no clobbering will occur.</p>
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
----_NmP-4a3807adb34bd6b8-Part_1--
