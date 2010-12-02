'''
Containers comparison and difference search
'''

__all__ = [
    'DictDiff',
    'SetDiff',
    ]

class DictDiff(object):
    """
    Compares two dicts and stores changes in attributes:
        * added {key:first_dict_value}
            first dict don't have this keys of second dict
        * removed {key:second_dict_value}
            second dict don't have this keys of first dict
        * changed  {key:(first_dict_value, second_dict_value)}
            both dicts have this keys but values are different
    """
    def __init__(self, old, new):
        added = self.added = {}
        removed = self.removed = {}
        changed = self.changed = {}
        newkeys = set(new)
        same = .0
        for (key, old_value) in old.iteritems():
            if key not in new:
                removed[key] = old_value
            else:
                new_value = new[key]
                if new_value != old_value:
                    changed[key] = (old_value, new_value)
                else:
                    same += 1
                newkeys.remove(key)
        for key in newkeys:
            added[key] = new[key]
        self.score = same / ( len(added) + len(changed) + len(added) + same )

    def __nonzero__(self):
        """
        DictDiff instance equals True if dicts have mismatches
        """
        return bool(self.added or self.removed or self.changed)

    def keys(self):
        """
        Returns set with mismatched keys
        """
        return set(self.added) | set(self.removed) | set(self.changed)

class SetDiff(object):
    """
    Compares two sets and stores changes in attributes:
        * added {key:first_dict_value}
            first set don't have this old_value of second set
        * removed {key:second_dict_value}
            second set don't have this old_value of first set
    """
    def __init__(self, old, new):
        new = set(new)
        old = set(old)
        self.added = frozenset(new - old)
        self.removed = frozenset(old - new)
        self.score = float(len(old & new)) / len(old | new)

    def __nonzero__(self):
        """
        DictDiff instance equals True if sets have mismatches
        """
        return bool(self.added or self.removed)

try:
    from .modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
except ImportError:
    pass
