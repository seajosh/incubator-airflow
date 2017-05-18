#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""job DateTime timezone aware

Revision ID: 2848ced31f28
Revises: 127d2bf2dfa7
Create Date: 2017-05-18 17:53:45.463247

"""

# revision identifiers, used by Alembic.
revision = '2848ced31f28'
down_revision = '127d2bf2dfa7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def alter(batch_op, name):
    batch_op.alter_column(name,
                          type_=sa.DateTime(timezone=True))

def upgrade():
    with op.batch_alter_table('chart') as batch_op:
        alter(batch_op, 'last_modified')

    with op.batch_alter_table('dag') as batch_op:
        alter(batch_op, 'last_scheduler_run')
        alter(batch_op, 'last_pickled')
        alter(batch_op, 'last_expired')

    with op.batch_alter_table('dag_pickle') as batch_op:
        alter(batch_op, 'created_dttm')

    with op.batch_alter_table('dag_run') as batch_op:
        alter(batch_op, 'execution_date')
        alter(batch_op, 'start_date')
        alter(batch_op, 'end_date')

    with op.batch_alter_table('import_error') as batch_op:
        alter(batch_op, 'timestamp')
        
    with op.batch_alter_table('job') as batch_op:
        alter(batch_op, 'start_date')
        alter(batch_op, 'end_date')
        alter(batch_op, 'latest_heartbeat')

    with op.batch_alter_table('known_event') as batch_op:
        alter(batch_op, 'start_date')
        alter(batch_op, 'end_date')

    with op.batch_alter_table('log') as batch_op:
        alter(batch_op, 'dttm')
        alter(batch_op, 'execution_date')

    with op.batch_alter_table('sla_miss') as batch_op:
        alter(batch_op, 'execution_date')
        alter(batch_op, 'timestamp')

    with op.batch_alter_table('task_fail') as batch_op:
        alter(batch_op, 'execution_date')
        alter(batch_op, 'start_date')
        alter(batch_op, 'end_date')

    with op.batch_alter_table('task_instance') as batch_op:
        alter(batch_op, 'execution_date')
        alter(batch_op, 'start_date')
        alter(batch_op, 'end_date')
        alter(batch_op, 'queued_dttm')

    with op.batch_alter_table('xcom') as batch_op:
        alter(batch_op, 'execution_date')
        alter(batch_op, 'timestamp')
        

def downgrade():
    pass
