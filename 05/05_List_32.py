new_recent_queue = []
next_recent_queue = []

next_queue_number = None

remaining_queue = []
# all_queues = []

qtime = []

for _ in range(int(input())):
    raw = input().strip().split(' ')
    cmd = raw[0]

    if cmd == 'reset':
        queue_number = int(raw[1])
        next_queue_number = queue_number

    elif cmd == 'new':
        time = int(raw[1])
        new_recent_queue = [next_queue_number, time]

        # all_queues.append(new_recent_queue)
        remaining_queue.append(new_recent_queue)

        print('ticket', next_queue_number)

        next_queue_number += 1

    elif cmd == 'next':
        queue_number, time = remaining_queue.pop(0)
        next_recent_queue = [queue_number, time]
        print('call', queue_number)

    elif cmd == 'order':
        time = int(raw[1])
        queue_number = next_recent_queue[0]
        dt = time - next_recent_queue[1]

        qtime.append(dt)

        print('qtime', queue_number, dt)

    elif cmd == 'avg_qtime':
        avg_qtime = round(sum(qtime)/len(qtime), 4)
        print('avg_qtime', avg_qtime)