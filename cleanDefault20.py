# Copyright: Arthur Milchior arthur@milchior.fr
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Feel free to contribute to this code on https://github.com/Arthur-Milchior/anki-clean-Default
# Addons number 683170394


from aqt.utils import showWarning
from anki.hooks import addHook
from aqt.qt import *
from anki.notes import Note
from anki.cards import Card
from aqt.utils import showWarning

defaultID= 1
nidToDeck={}
"""associating to nid's a non-default deck of some card. If possible, a card selected, if not, an arbitrary card."""

def run(browser):
    cards=[Card(browser.col,cid) for cid in browser.selectedCards()]
    for card in cards:
        prepare(card, browser)
    for card in cards:
        cleanCard(card, browser)

def prepare(card, browser):
    """state that cid's note's deck is card's deck if it is not default"""
    if card.did!= defaultID:
        noteToDeck(card.nid,browser,  did=card.did)
        

def noteToDeck(nid,browser, did=None):
    """adds the did to nidToDeck. Either the given one, or one from a sibling
    card not in default.

    Do not add anything if nid already in nidToDeck.
    Return the did
    """
    if nid in nidToDeck:
        return nidToDeck[nid]
    if did:
        nidToDeck[nid]=did
        return did

    note=Note(browser.col,id=nid)
    cards = note.cards()
    for card in cards:
        if card.did != defaultID:
            nidToDeck[nid]=card.did
            return card.did
    else:
        return None

def cleanCard(card,browser):
    if card.did != defaultID:
        return
    did=noteToDeck(card.nid, browser)
    if not did:
        print("note "+str(card.nid)+" is entirely in Default")
        return
    card.did = did
    card.flush()

def setupMenu(browser):
    a = QAction("Clean Default", browser)
    browser.connect(a, SIGNAL("triggered()"), lambda e=browser: run(e))
    browser.form.menuEdit.addSeparator()
    browser.form.menuEdit.addAction(a)

addHook("browser.setupMenus", setupMenu)

