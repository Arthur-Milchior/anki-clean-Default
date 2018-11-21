# Clean the default deck
Move card's currently in Default Deck to their correct deck. At least,
to the best guessed deck
## Rationale
If a card lose it decks, it goes to the default deck.  This add-on
allows to correct this error, and putting those cards back into their
deck. At least, the add-on tries to guess which is the correct deck.

## Usage
In the browser:
* select notes you want to move from default to their correct deck
* Select "Edit">"Clean default"
## Internal
The rules to determine to which deck the add-on move a card are as follows:
* if the card's deck is not default, do nothing
* Otherwise, if there are siblings selected in a non-default deck, move the card to one of such deck
* Otherwise if there are non-selected sibling in non-deck deck, move the card to one of such deck


## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-clean-default
Addon number| [683170394](https://ankiweb.net/shared/info/683170394)

