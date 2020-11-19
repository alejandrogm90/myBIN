#! /bin/bash

#
#
#       Copyright 2019 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

function try()
{
    [[ $- = *e* ]]; SAVED_OPT_E=$?
    set +e
}

function throw()
{
    exit $1
}

function catch()
{
    export ex_code=$?
    (( $SAVED_OPT_E )) && set +e
    return $ex_code
}

function throwErrors()
{
    set -e
}

function ignoreErrors()
{
    set +e
}

export AnException=100
export AnotherException=101

# start with a try
try
(   # open a subshell !!!
    echo "do something"
    [ someErrorCondition ] && throw $AnException

    echo "do something more"
    executeCommandThatMightFail || throw $AnotherException

    throwErrors # automaticatly end the try block, if command-result is non-null
    echo "now on to something completely different"
    executeCommandThatMightFail

    echo "it's a wonder we came so far"
    executeCommandThatFailsForSure || true # ignore a single failing command

    ignoreErrors # ignore failures of commands until further notice
    executeCommand1ThatFailsForSure
    local result = $(executeCommand2ThatFailsForSure)
    [ result != "expected error" ] && throw $AnException # ok, if it's not an expected error, we want to bail out!
    executeCommand3ThatFailsForSure

    echo "finished"
)
# directly after closing the subshell you need to connect a group to the catch using ||
catch || {
    # now you can handle
    case $ex_code in
        $AnException)
            echo "AnException was thrown"
        ;;
        $AnotherException)
            echo "AnotherException was thrown"
        ;;
        *)
            echo "An unexpected exception was thrown"
            throw $ex_code # you can rethrow the "exception" causing the script to exit if not caught
        ;;
    esac
}
