import json

from util.lua_exchange import LuaExchange

table = '''return {
--[[
    Notes: support load value only.
]]

--Notes: all notes will be ignored.

    test = {
        ["1"] = {-0, 5},
        [{2}] = {7, 0xabc},
        [3] = {19.345, -27},
        [4.0] = {-19.123, 0x123},
    },
    path = '$A',
    remark = [[
    just a remark.
    ]],
    layer = {
        skin_a = 0,
        pants_a = 100,
        cap_a = 500,
        shoulder_a = 500,
        weapon_a = 700,
    }
}
'''

obj = LuaExchange.from_lua(table[table.find('return') + 6:])
print(obj)
print('return %s' % LuaExchange.to_lua(obj))
print(json.dumps(LuaExchange.from_lua('{test={ -1, 0x2, 3.0, \'123\'}}')))
