# -*- coding: utf-8 -*-

""" The observers. """

import pelita.datamodel as uni

__docformat__ = "restructuredtext"


class AbstractViewer(object):

    def observe(self, round_, turn, universe, events):
        raise NotImplementedError(
                "You must override the 'observe' method in your viewer")

class DevNullViewer(object):
    """ A viewer that simply ignores everything. """

    def observe(self, round_, turn, universe, events):
        pass

class AsciiViewer(AbstractViewer):

    def observe(self, round_, turn, universe, events):
        print ("Round: %i Turn: %i Score: %i:%i"
        % (round_, turn, universe.teams[0].score, universe.teams[1].score))
        print ("Events: %r" % [str(e) for e in events])
        print universe.compact_str
        if uni.TeamWins in events:
            team_wins_event = events.filter_type(uni.TeamWins)[0]
            print ("Game Over: Team: '%s' wins!" %
            universe.teams[team_wins_event.winning_team_index].name)
