<?php

use yii\db\Migration;

class m171010_161405_add_user_table extends Migration
{

    public function safeUp()
    {
        $this->addColumn('user', 'termsbox_accepted', $this->boolean()->defaultValue(false)->null());

        $sql = 'UPDATE user u ';
        $sql .= 'LEFT JOIN contentcontainer_setting cs ON u.contentcontainer_id=cs.contentcontainer_id AND cs.module_id="termsbox" AND cs.name="timestamp" ';
        $sql .= 'SET u.termsbox_accepted=1 ';
        $sql .= 'WHERE cs.value=:timestamp AND cs.id IS NOT NULL';
        $this->db->createCommand($sql, [':timestamp' => Yii::$app->getModule('termsbox')->settings->get('timestamp')])->execute();

        $this->delete('contentcontainer_setting', ['module_id' => 'termsbox', 'name' => 'timestamp']);
    }

    public function safeDown()
    {
        echo "m171010_161405_add_user_table cannot be reverted.\n";

        return false;
    }

    /*
      // Use up()/down() to run migration code without a transaction.
      public function up()
      {

      }

      public function down()
      {
      echo "m171010_161405_add_user_table cannot be reverted.\n";

      return false;
      }
     */
}
