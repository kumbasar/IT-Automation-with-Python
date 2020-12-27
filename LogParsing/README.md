# Generate report from log file

This script generates user and error csv reports from `syslog.log` file.
## Usage

```bash
./server_check.py <log file>
```
## Example log file

A `syslog.log` file:

```
Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)
Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)
Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)
Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)
Jan 31 01:29:16 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)
```
## Example outputs

### `error_message.csv`

```csv
Error,Count
Timeout while retrieving information,15
Connection to DB failed,13
Tried to add information to closed ticket,12
Permission denied while closing ticket,10
The ticket was modified while updating,9
Ticket doesn't exist,7
```

### `user_statistics.csv`

```csv
Username,INFO,ERROR
ac,2,2
ahmed.miller,2,4
blossom,2,6
bpacheco,0,2
breee,1,5
britanni,1,1
enim.non,2,3
flavia,0,5
jackowens,2,4
kirknixon,2,1
mai.hendrix,0,3
mcintosh,4,3
mdouglas,2,3
montanap,0,4
noel,6,3
nonummy,2,3
oren,2,7
rr.robinson,2,1
sri,2,2
xlg,0,4
```