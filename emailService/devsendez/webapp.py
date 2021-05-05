# ----------------------------------------------------------------------------
# Dev Send EZ Server Routes
# Author: Ren Demeis-Ortiz
# Description: Handles post requests to the server
# ----------------------------------------------------------------------------

#from flask import Flask, request, redirect
from devsendez.sendEmail import sendEmail




sendEmail('demeisol@oregonstate.edu', 'me', 'test@test.com', 'testing', 'test message body', "<!DOCTYPE html><html><body><h1>Test Header</h1></body></html>")