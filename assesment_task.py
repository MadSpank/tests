DEVICE_STATES = {
    'out_of_use': 'OUT_OF_USE',
    'in_storage': 'IN_STORAGE',
    'in_use': 'IN_USE'
    }

LISTING_TITLES = {
    'deny': 'DSNs under DENY LIST',
    'allow': 'DSNs under ALLOW LIST'
    }

def device_security(input_log):
    ds_result = {}
    func_result = {
        LISTING_TITLES['deny']: [],
        LISTING_TITLES['allow']: [],
        }

    for log in input_log:
        timestamp, dsn, _, _, end_state = log.split()
        if dsn not in ds_result.keys():
            ds_result[dsn] = [timestamp, end_state]
        else:
            if ds_result[dsn][0] < timestamp:
                ds_result[dsn][0], ds_result[dsn][1] = timestamp, end_state

    for dsn, details in ds_result.items():
        if details[1] == DEVICE_STATES['in_storage']:
            func_result[LISTING_TITLES['allow']].append(dsn)

        if details[1] == DEVICE_STATES['out_of_use']:
            func_result[LISTING_TITLES['deny']].append(dsn)

    with open('OutputFile.txt', 'w') as output_file:
        output_file.write(LISTING_TITLES['deny'] + '\n')
        output_file.write('\n'.join(func_result[LISTING_TITLES['deny']]) + '\n')

        output_file.write('\n' + LISTING_TITLES['allow'] + '\n')
        output_file.write('\n'.join(func_result[LISTING_TITLES['allow']]) + '\n')


if __name__ == '__main__':
    file = 'input_log.txt'
    with open(file, 'r') as f:
        device_security(f)