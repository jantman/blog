Title: Universal Standardized Message/Alert/Notification Bus
Date: 2014-05-13 08:44
Author: Jason Antman
Category: Ideas and Rants
Tags: 
Slug: universal-standardized-message-alert-notification-bus
Summary: <<<<< summary goes here >>>>>>>
Status: draft

content (written in MarkDown - http://daringfireball.net/projects/markdown/syntax )

A universal message/alert/notification bus and format

send notifications/alerts/messages as json
source
severity (syslog)
program name
host name
application name
human-readable text
current value metric
threshold metric
min/max metrics
free-form application-specific data
event type (enum?)

send via AMQP or HTTP, or other protocols?
goes into a broker
subscriptions from real people
subscriptions from services/applications
