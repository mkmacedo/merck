//abrir em um editor de texto e dar replace em "teste" pela empresa que deseja excluir do projeto no wise
//flowtemplatevariable
DELETE FROM wisecapture.flowtemplatevariable WHERE idtenant = 'teste' AND flowtemplateid = 'unknown' AND field = 'tipoDocumento';

//flowtemplate
DELETE FROM wisecapture.flowtemplate WHERE idtenant = 'teste' AND flowtemplateid = 'unknown';
DELETE FROM wisecapture.flowtemplate WHERE idtenant = 'teste' AND flowtemplateid = 'not_identified';

//tasktablecolumn
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'action';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'usersEditingLine';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'keyVariableValue.razaoSocialPrestador';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'keyVariableValue.businessDocType';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'lastStatusUpdate';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'keyVariableValue.numeroNota';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'flowId';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'status';
DELETE FROM wisecapture.tasktablecolumn WHERE idtenant = 'teste' AND field = 'name';

//tasktemplate
DELETE FROM wisecapture.tasktemplate WHERE idtenant = 'teste' AND flowtemplateid = 'unknown' AND tasktemplateid = 'email';
DELETE FROM wisecapture.tasktemplate WHERE idtenant = 'teste' AND flowtemplateid = 'unknown' AND tasktemplateid = 'ocr';

//wiseuser
DELETE FROM wisecapture.wiseuser WHERE idtenant = 'teste' AND username = 'fabio.mazzo';

//menu
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'Users';
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'Flow';
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'TasksReady';
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'Logout';
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'Dashboard';
DELETE FROM wisecapture.menu WHERE idtenant = 'teste' AND name = 'TableUpload';

//tenantconfiguration
DELETE FROM wisecapture.tenantconfiguration WHERE idtenant = 'teste';

//workflowstatusconfig
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'NOT_APPLICABLE';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'USER_DISCARDED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'RETURNED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'NO_DOCUMENT';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'ON_HOLD';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'PROCESSING';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'ERROR';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'DISCARDED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = '**ALL**';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'WAITING';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'KLINK_DISCARDED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'PENDING';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'DONE';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'CANCELED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'CLOSED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'KLINK_REVIEW';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'KLINK_DISCARDED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'VALIDATED';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'SPAM';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'DONE';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'PENDING';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'ERROR';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'task' AND status = 'READY';
DELETE FROM wisecapture.workflowstatusconfig WHERE idtenant = 'teste' AND workflowentity = 'flow' AND status = 'DUPLICATED';

//flowtablecolumn
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'createdDate';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'businessDocType';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'id';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'status';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'qtyTasksDone';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'qtyTasks';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'usersEditingLine';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'keyVariableValue.numeroNota';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'action';
DELETE FROM wisecapture.flowtablecolumn WHERE idtenant = 'teste' AND field = 'keyVariableValue.razaoSocialPrestador';

//ocrconfiguration
DELETE FROM wisecapture.ocrconfiguration WHERE idtenant = 'teste' AND templatename = 'unknown' AND version = '1.0';






