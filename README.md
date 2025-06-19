# test-github-actions

TODO:

- workflow to verify the strategy PR(on PR open)
  - check only 1 file was added to the correct place and no other was modified
  - check strategy code(could maybe be deferred to an external python/bash script)
    - checks are based on the language chosen, so make this a language specific check
    - it's formatted and runs correctly
    - don't generate errors in the expected contexts
    - doesn't use any custom library, must rely only on native ones, in addition to maybe a few exceptions
    - doesn't reach to any external resource, like any network or file access
    - must use a reasonable time, memory, heap and other resources to execute
    - run it against a "test tournment"(predictable size, agains a few known strategies)
      - check if runs correctly
      - prevent duplicates
        - save the strategy results and choices as byte strings signatures
          - use it to compare if there's any other existing one with the same behavior(result and signature)
- workflow to run the tournment(on PR merge)
  - must ensure only 1 run at the time
  - run the submitted strategy against all the other existing strategies
  - cache the result for further reuse
    - use a local sqlite db or json?
    - consider tournments with "random noise"
      - save results and signatures by parts and inject "seed noises" only in between those parts, which would make the results predictable in between those segments(future optimization, given this might not be very feasible due to the amount of cache miss and overhead)
        - save the results in a tree like structure, to be able to identify the cached outcomes per segment and also grow each for each new random
  - P.S.: later it might need a refactor to work on cronjob with multiple new strategies instead of only one
- codeowners file to protect all the "non-public" files from being able to be merged by "non-admin"
- repo branch protections to all branches/files that are not the "strategies" branch and folder
